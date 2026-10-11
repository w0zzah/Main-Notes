A saved query that acts like a table. Stores no data — reads from the underlying (base) tables every time. [[SELECT]] · [[Update]] · [[DELETE]] · [[TRIGGERS]]

## Template
```sql
CREATE VIEW view_name AS
SELECT ...;

SELECT * FROM view_name WHERE ...;   -- query it like a table

DROP VIEW view_name;
```

## Rules
- The view's column names come from the SELECT → aggregates need an alias (`COUNT(*) AS regno`).
- Changes to base tables show up in the view automatically.
- INSERT / UPDATE / DELETE on an updatable view change the **base table**.

## When can you UPDATE / DELETE / INSERT on a view?
**Standard SQL**
- One underlying table and the view includes that table's primary key (or a candidate key)
- You CANT update views built on multiple tables (joins) — generally not updatable
- You CANT update views using `GROUP BY`, aggregates (`COUNT`, `SUM`…), `DISTINCT`, `IN`, `ANY`, `ALL`, `EXISTS`

**Oracle**
- Single table views without aggregates / GROUP BY / set ops / DISTINCT are updatable even without the PK (Lab 3 Q5 below)
- Some multi-table views are updatable if they contain a table's PK — only the columns of that one table. Check which columns:

```sql
SELECT column_name, updatable
FROM   user_updatable_columns
WHERE  table_name = UPPER('view_name');
```

**Fix for a non-updatable view:** `INSTEAD OF` trigger — runs your own statements on the base tables in place of the update (Lab 4 Q3 below). INSTEAD OF triggers only work on views.

## Examples (from lectures / labs)
View over a join (lecture) — COMEDIES: movie number, title, director number and name for all comedies
```sql
CREATE VIEW comedies AS
SELECT mnumber, title, dnumber, lname, fname
FROM   movie, director
WHERE  director = dnumber AND type = 'comedy';
```
(this one joins two tables → not updatable in standard SQL)

Single table, no PK — Oracle still allows the update (Lab 3 Q5)
```sql
CREATE VIEW emps AS
SELECT lname, fname, bdate
FROM   employee
WHERE  reg_org IS NOT NULL;

UPDATE emps
SET    bdate = '25-jul-2011'
WHERE  fname = 'Anna' AND lname = 'Simmons';
-- works in Oracle, changes the EMPLOYEE table
-- standard SQL: NOT allowed, the PK (ird) isn't in the view
```

Aggregate view — can query, can't modify (Lab 3 Q6)
```sql
CREATE VIEW veh_info AS
SELECT vehicle.plates, make, model, COUNT(*) AS regno
FROM   vehicle JOIN registration ON registration.plates = vehicle.plates
GROUP BY vehicle.plates, make, model;

SELECT plates FROM veh_info WHERE regno >= 3;   -- fine

DELETE FROM veh_info WHERE plates = 'FO2341';   -- ERROR: aggregate view
```

Multi-table + aggregate view, fixed with INSTEAD OF (Lab 4 Q3)
```sql
CREATE VIEW multireg AS
SELECT org_number, M.lname, M.fname, COUNT(*) AS total_emp
FROM   reg_org, employee E, employee M
WHERE  manager = M.ird AND E.reg_org = org_number
GROUP BY org_number, M.lname, M.fname;

-- a) fails: view is not updatable (multi-table + GROUP BY)
UPDATE multireg
SET    lname = 'Right', fname = 'John'
WHERE  org_number = '1303';

-- b) trigger that does the real change on REG_ORG instead
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

-- c) the same UPDATE now works: "1 row updated."
```
