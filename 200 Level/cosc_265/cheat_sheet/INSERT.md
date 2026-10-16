Adds new rows to a table. [[Update]] · [[DELETE]] · [[CREATE TABLE]] · [[Schemas]]

## Template
```sql
-- all columns, in CREATE TABLE order
INSERT INTO table_name
VALUES (val1, val2, ...);

-- only some columns (the rest become NULL / DEFAULT)
INSERT INTO table_name (col1, col2)
VALUES (val1, val2);

-- many rows from a query
INSERT INTO table_name (col1, col2)
SELECT ...;
```

## Rules
- Without a column list, values must be in the **same order as the columns in CREATE TABLE**, and every column needs a value — write `null` for unknowns. Check the order with `describe table_name;`
- With a column list, left-out columns become NULL (or their DEFAULT). Can't leave out a NOT NULL column.
- Text and dates go in single quotes: `'Anna'`, `'01-jul-2011'`. Numbers don't.
- Apostrophe inside a string → double it: `'O''Toole'`.
- The row must satisfy every constraint: PK must be unique, FK value must exist in the parent table, CHECKs must pass.
- INSERT ... SELECT: no `VALUES` keyword, and the SELECT's columns must line up with the column list.
- Run a script of inserts in SQL*Plus with `@populate-tables` → see [[SQLPlus]]

## Examples (from lectures / labs)
All columns, NULL for unknowns (Lab 1, OWNER)
```sql
INSERT INTO owner
VALUES ('BA789256', 58743344, 'Anna', 'B', 'Simmons',
        '21 Aorangi Rd Christchurch', '21-jan-58', 'f', null, '3381275');
```

All columns, NULL country (Lab 3 Q4b) — registration for TX9283 on 1 July 2011 by employee 21321322 of org 1352, DRR 169654, cost $137.85
```sql
INSERT INTO registration
VALUES ('TX9283', 21321322, 1352, '01-jul-2011', null, 169654, 137.85);
```

Only some columns known (lecture Ex 2) — new customer, only number and name known
```sql
INSERT INTO customer (cnumber, lname, fname)
VALUES (127, 'Smith', 'John');
```

Many rows from a query (lecture Ex 3) — table holding number, title, year and director's name for every movie
```sql
CREATE TABLE movie_info
(mnumber integer, title varchar(50), year integer,
 dlname varchar(16), dfname varchar(15));

INSERT INTO movie_info (mnumber, title, year, dlname, dfname)
SELECT mnumber, title, year, lname, fname
FROM   movie, director
WHERE  director = dnumber;
```

## Inserting inside a trigger
Use `:new.col` for the values of the row that fired the trigger (Lab 4 Q2 — new owner added to OWNER2):
```sql
INSERT INTO owner2
VALUES (:new.ownerid, olname, ofname, 1);
```
Full trigger → see [[TRIGGERS]]
