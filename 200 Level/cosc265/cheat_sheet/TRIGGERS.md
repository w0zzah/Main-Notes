Code that runs automatically when an INSERT / UPDATE / DELETE happens on a table or view. [[VIEW]] · [[Update]] · [[INSERT]] · [[DELETE]] · [[CREATE TABLE]]

## Template
```sql
CREATE [OR REPLACE] TRIGGER trigger_name
{BEFORE | AFTER | INSTEAD OF}
{INSERT | DELETE | UPDATE [OF col1, col2]} [OR INSERT | OR DELETE | OR UPDATE ...]
ON table_or_view
FOR EACH ROW
[WHEN (condition)]
DECLARE
    var_name type;
    var_name type := 0;
BEGIN
    statements;
END;
/
```
The `/` on its own line runs it in SQL*Plus.

## Parts
- **Event** — the INSERT / UPDATE / DELETE that fires it
- **Condition** — the WHEN test
- **Action** — the BEGIN ... END body

## Choosing the type
| Need | Use |
|---|---|
| Stop a bad insert/update (validate, raise error) | `BEFORE ... FOR EACH ROW` |
| Keep another table in sync (totals, counts) | `AFTER ... FOR EACH ROW` |
| Make a non-updatable view updatable | `INSTEAD OF ... ON view` |
| Only when a certain column changes | `UPDATE OF col` |

Row-level (`FOR EACH ROW`) = runs once per row changed. Statement-level (leave out FOR EACH ROW) = runs once per statement.

## Rules
- `:new.col` = new values (INSERT, UPDATE). `:old.col` = old values (UPDATE, DELETE). INSERT has no :old, DELETE has no :new.
- **In WHEN: no colon** → `WHEN (new.dno IS NOT NULL)`. **In the body: colon** → `:new.dno`.
- WHEN only on row-level BEFORE/AFTER triggers, and it **can't contain a query**.
- `INSTEAD OF` triggers only on views.
- Body can't contain DDL (CREATE/ALTER/DROP) or transaction control.
- Can't generally read from / modify the table the trigger is on (mutating table) — there are exceptions.
- A SELECT in the body must use `INTO` a variable: `SELECT cost INTO product_cost FROM ...` — and must return exactly one row.
- Declare variables in `DECLARE` before `BEGIN`.
- Trigger names must be unique in the database.
- Can't edit a trigger's body with ALTER → use `CREATE OR REPLACE TRIGGER`.
- Slides sometimes write a single statement with no BEGIN/END (totalsal1–3). If Oracle complains, wrap the body in `BEGIN ... END;`.

## PL/SQL bits used in triggers
```sql
IF x = 0 THEN
    ...;
ELSIF y THEN
    ...;
ELSE
    ...;
END IF;

-- which event fired it (trigger on INSERT OR DELETE OR UPDATE)
IF INSERTING THEN ... ELSIF DELETING THEN ... ELSIF UPDATING('COL') THEN ... END IF;

-- reject the statement
RAISE_APPLICATION_ERROR(-20000, 'message');   -- number between -20000 and -20999 in the examples
```

## Managing triggers
```sql
SHOW ERRORS;                            -- see compile errors after "created with compilation errors"
SHOW ERRORS TRIGGER trigger_name;
DROP TRIGGER trigger_name;
ALTER TRIGGER trigger_name ENABLE;      -- or DISABLE / COMPILE
```

## Examples (from lectures / labs)
### AFTER — keep a derived total correct (lecture, TOTAL_SAL in DEPARTMENT)
Insert:
```sql
CREATE TRIGGER totalsal1
AFTER INSERT ON employee
FOR EACH ROW
WHEN (new.dno IS NOT NULL)
UPDATE department
SET    total_sal = total_sal + :new.salary
WHERE  dno = :new.dno;
/
```
Update of salary:
```sql
CREATE TRIGGER totalsal2
AFTER UPDATE OF salary ON employee
FOR EACH ROW
WHEN (new.dno IS NOT NULL)
UPDATE department
SET    total_sal = total_sal + :new.salary - :old.salary
WHERE  dno = :new.dno;
/
```
Delete:
```sql
CREATE TRIGGER totalsal3
AFTER DELETE ON employee
FOR EACH ROW
WHEN (old.dno IS NOT NULL)
UPDATE department
SET    total_sal = total_sal - :old.salary
WHERE  dno = :old.dno;
/
```
Employee changes department (two statements → BEGIN/END):
```sql
CREATE TRIGGER totalsal4
AFTER UPDATE OF dno ON employee
FOR EACH ROW
BEGIN
    UPDATE department
    SET    total_sal = total_sal + :new.salary
    WHERE  dno = :new.dno;
    UPDATE department
    SET    total_sal = total_sal - :old.salary
    WHERE  dno = :old.dno;
END;
/
```

### AFTER INSERT — insert or update a summary table (Lab 4 Q2, OWNER2)
New row in OWNS → if owner not in OWNER2 add them with 1 car, else add 1 to their count.
```sql
CREATE OR REPLACE TRIGGER change_owner2
AFTER INSERT ON owns
FOR EACH ROW
WHEN (new.datesold IS NULL)
DECLARE
    check_tuple integer := 0;
    olname varchar(15);
    ofname varchar(15);
BEGIN
    SELECT COUNT(*) INTO check_tuple
    FROM   owner2
    WHERE  dr_lic = :new.ownerid;

    IF check_tuple = 0 THEN            -- new owner, not in OWNER2 yet
        SELECT lname, fname INTO olname, ofname
        FROM   owner
        WHERE  dr_lic = :new.ownerid;
        INSERT INTO owner2
        VALUES (:new.ownerid, olname, ofname, 1);
    ELSE                               -- existing owner, one more car
        UPDATE owner2
        SET    no_cars = no_cars + 1
        WHERE  dr_lic = :new.ownerid;
    END IF;
END;
/
```
Test it: `SELECT * FROM owner2;` → insert into OWNS → `SELECT * FROM owner2;` again, count went up.

### BEFORE INSERT — reject bad data using another table (lecture lab test, ORDER_ITEM)
CHECK can't look at COMP table, so a trigger does it.
```sql
CREATE OR REPLACE TRIGGER check_price
BEFORE INSERT ON order_item
FOR EACH ROW
DECLARE
    product_cost float;
BEGIN
    SELECT cost INTO product_cost
    FROM   comp
    WHERE  code = :new.product;
    IF :new.product_cost <> (product_cost * :new.quantity) THEN
        RAISE_APPLICATION_ERROR(-20000, 'Cannot add this tuple: the price is incorrect!');
    END IF;
END;
/
```

### BEFORE INSERT — only one account of each type (lecture lab test, BANK)
Same rule could be done with `UNIQUE (type, customer)` → see [[ALTER-DROP]]
```sql
CREATE OR REPLACE TRIGGER insert_account
BEFORE INSERT ON account
FOR EACH ROW
DECLARE
    ac_num integer;
BEGIN
    SELECT COUNT(*) INTO ac_num
    FROM   account
    WHERE  customer = :new.customer AND type = :new.type;
    IF ac_num = 1 THEN
        RAISE_APPLICATION_ERROR(-20201, 'An account of this type already exists');
    END IF;
END;
/
```

### INSTEAD OF — update a non-updatable view (Lab 4 Q3, MULTIREG)
```sql
CREATE TRIGGER update_view
INSTEAD OF UPDATE ON multireg
FOR EACH ROW
DECLARE
    managerno char(8);
BEGIN
    SELECT ird INTO managerno
    FROM   employee
    WHERE  lname = :new.lname AND fname = :new.fname;

    UPDATE reg_org
    SET    manager = managerno
    WHERE  org_number = :new.org_number;
END;
/
```
View definition → see [[VIEW]]

### Several events in one trigger — audit (lecture)
```sql
CREATE TRIGGER audit_trigger
BEFORE INSERT OR DELETE OR UPDATE ON classified_table
FOR EACH ROW
BEGIN
    IF INSERTING THEN
        INSERT INTO audit_table
        VALUES (USER || ' is inserting' || ' new key: ' || :new.key);
    ELSIF DELETING THEN
        INSERT INTO audit_table
        VALUES (USER || ' is deleting' || ' old key: ' || :old.key);
    ELSIF UPDATING('FORMULA') THEN
        INSERT INTO audit_table
        VALUES (USER || ' is updating' || ' old formula: ' || :old.formula
                     || ' new formula: ' || :new.formula);
    ELSIF UPDATING THEN
        INSERT INTO audit_table
        VALUES (USER || ' is updating' || ' old key: ' || :old.key || ' new key: ' || :new.key);
    END IF;
END;
/
```
