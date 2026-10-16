An access structure that speeds up searching on a column. [[CREATE TABLE]] · [[ALTER-DROP]]

## Template
```sql
CREATE INDEX index_name
ON table_name (col1 [, col2 ...]);

DROP INDEX index_name;
```

## Rules
- Oracle creates indexes automatically for primary keys and UNIQUE (secondary) keys — don't index those yourself.
- Good candidates: columns used often in **search (WHERE) and join conditions**.
- Bad candidates: columns that are **frequently updated** (the index has to be updated too).
- Create indexes before the tables are populated.

## Examples (from lectures / labs)
Single column (Lab 3 Q7) — IYEAR on VEHICLE.year
```sql
CREATE INDEX iyear
ON vehicle (year);
```

Single column (lecture) — CNO on CUSTOMER.cnumber
```sql
CREATE INDEX cno
ON customer (cnumber);
```

Two columns (lecture) — CNAME on CUSTOMER last and first name
```sql
CREATE INDEX cname
ON customer (lname, fname);
```
