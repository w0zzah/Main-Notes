Change an existing table's columns or constraints, or remove a table. [[CREATE TABLE]] · [[INDEX]] · [[VIEW]] · [[TRIGGERS]]

## Template
```sql
-- add a column
ALTER TABLE table_name ADD col_name type;

-- change a column
ALTER TABLE table_name MODIFY col_name new_spec;

-- add a constraint
ALTER TABLE table_name ADD CONSTRAINT name CHECK (condition);
ALTER TABLE table_name ADD CONSTRAINT name UNIQUE (col1, col2);
ALTER TABLE table_name ADD FOREIGN KEY (col) REFERENCES other_table;

-- remove a constraint
ALTER TABLE table_name DROP CONSTRAINT name;

-- remove a table
DROP TABLE table_name;
DROP TABLE table_name CASCADE CONSTRAINTS;
```

Other DROPs: `DROP VIEW name;` · `DROP INDEX name;` · `DROP TRIGGER name;`

## Rules
- A newly added column is NULL in every existing row → you can't add it as `NOT NULL`. Fill it in afterwards with [[Update]].
- `DROP TABLE` removes the data AND the definition — the table can't be used any more.
- If other tables have FKs pointing at the table, plain `DROP TABLE` fails → drop those tables too, or use `CASCADE CONSTRAINTS`.
- `DROP SCHEMA name CASCADE` deletes every object in the schema; `RESTRICT` only drops if empty.
- To remove all rows but keep the table → `DELETE FROM table_name;` (see [[DELETE]]), not DROP.

## Tables that reference each other
EMPLOYEE.reg_org → REG_ORG and REG_ORG.manager → EMPLOYEE (Lab 1)
1. Create EMPLOYEE without the FK
2. Create REG_ORG (with its FK to EMPLOYEE)
3. Populate both
4. Then add the missing FK:
```sql
ALTER TABLE employee
ADD FOREIGN KEY (reg_org) REFERENCES reg_org;
```
If the FK is added before populating, neither table can be filled — each insert needs a matching row in the other table.

## Examples (from lectures / labs)
Add a column (lecture)
```sql
ALTER TABLE employee
ADD job varchar(12);
```

Add a CHECK table constraint (Lab 4 Q1)
```sql
ALTER TABLE vehicle_type
ADD CONSTRAINT constr_example CHECK (no_pass BETWEEN 0 AND 6);
```

Add a UNIQUE constraint — customer can only have one account of each type (lecture lab test, BANK)
```sql
ALTER TABLE account
ADD CONSTRAINT one_account UNIQUE (type, customer);
```
(the same rule can also be done with a trigger — INSERT_ACCOUNT in [[TRIGGERS]])

Drop tables (lecture / Lab 1)
```sql
DROP TABLE dependent;
DROP TABLE owns CASCADE CONSTRAINTS;
```
