Defines a new table: columns, types, keys and constraints. [[ALTER-DROP]] · [[INSERT]] · [[Schemas]] · [[TRIGGERS]]

## Template
```sql
CREATE TABLE table_name
(col_name  type  [NOT NULL] [DEFAULT value] [PRIMARY KEY]
                 [REFERENCES other_table[(col)]]
                 [CONSTRAINT name CHECK (condition)],
 col_name  type ...,
 [CONSTRAINT name] PRIMARY KEY (col1, col2),
 [CONSTRAINT name] FOREIGN KEY (col) REFERENCES other_table[(col)]
                   [ON DELETE CASCADE | ON DELETE SET NULL],
 [CONSTRAINT name] UNIQUE (col1, col2),
 [CONSTRAINT name] CHECK (condition));
```

Copy a table / make one from a query:
```sql
CREATE TABLE table_name AS
SELECT ...;
```

## Checklist (lecture)
- What attributes are stored? What types?
- Which columns make the primary key?
- Any foreign keys?
- Which columns can't be NULL? Which can't have duplicates (UNIQUE)?
- Any default values?
- Any limits on allowed values (CHECK)?

## Data types (Oracle)
- `integer`, `float`, `NUMBER(p,s)` — p = total digits, s = decimal digits. `NUMBER(17,12)` → 5 integer digits, 12 decimal
- `char(n)` fixed length, `varchar(n)` variable length
- `date` — default format `'dd-mon-yy'` e.g. `'21-jan-58'`, `'01-jul-2011'`

## Rules
- Attribute constraint = written on the same line as the column, can only use that one column.
- Constraint on two columns of the same table (e.g. `born <= died`) must be a table constraint (after all columns, or via ALTER TABLE).
- Composite primary key (more than one column) must be a table constraint: `PRIMARY KEY (plates, color)`.
- Constraint using columns from more than one table → not possible in Oracle, use a [[TRIGGERS|trigger]].
- `REFERENCES table` with no column = references that table's primary key.
- FK column type must match the PK it points to (e.g. `plates varchar(6)` in both).
- You can't create an FK to a table that doesn't exist yet. Two tables pointing at each other (EMPLOYEE ↔ REG_ORG): create both without one FK, populate, then add it with ALTER TABLE → see [[ALTER-DROP]].
- Name your constraints (`CONSTRAINT check_type ...`) so they're easy to find/drop later.
- Comments: `/* ... */` multi-line, `--` single line.
- Names: max 30 chars, start with a letter, no reserved words, can't start with `sys_`, case insensitive (except inside strings).
- SQL tables are multisets (duplicate rows allowed) unless you use PRIMARY KEY / UNIQUE (or DISTINCT in a query).

## Referential integrity options
- Standard SQL: `ON DELETE` / `ON UPDATE` with `SET NULL`, `CASCADE`, `SET DEFAULT`, `RESTRICT`
- **Oracle only supports `ON DELETE CASCADE` and `ON DELETE SET NULL`**

```sql
CONSTRAINT dirfk FOREIGN KEY (director) REFERENCES director(dnumber)
    ON DELETE SET NULL
```

## Not supported by Oracle
- `CREATE DOMAIN` — use CHECK on the column instead
- `CREATE ASSERTION` (constraints over several tables) — use a trigger
- Subqueries (nested SELECT) inside CHECK — use a trigger

## Examples (from lectures / labs)
Attribute constraints + table constraints (lecture, DIRECTOR)
```sql
CREATE TABLE director
(dnumber integer NOT NULL CONSTRAINT dir_pk PRIMARY KEY,
 lname   varchar(16) NOT NULL,
 fname   varchar(15),
 born    integer CONSTRAINT dir_born CHECK (born BETWEEN 1880 AND 1990),
 died    integer CONSTRAINT dir_died CHECK (died > 1930),
 gender  varchar(1)
 CONSTRAINT gender_check check (gender in ('m', 'f', 'n')),
 CONSTRAINT corr_years CHECK (born <= died));
```

DEFAULT, two FKs, named CHECK (lecture, DVD)
```sql
CREATE TABLE dvd
(code     integer NOT NULL,
 movie    integer NOT NULL,
 pdate    date,
 times    integer DEFAULT 0,
 customer integer,
 hiredate date,
 PRIMARY KEY (code),
 FOREIGN KEY (customer) REFERENCES customer(cnumber),
 FOREIGN KEY (movie) REFERENCES movie,
 CONSTRAINT check_times CHECK (times >= 0));
```

Composite PK, inline REFERENCES (lecture, STARS)
```sql
CREATE TABLE stars
(movie integer NOT NULL REFERENCES movie(mnumber),
 star  integer NOT NULL REFERENCES star(snumber),
 role  varchar(20) NOT NULL,
 PRIMARY KEY (movie, star, role));
```

CHECK with IN list, composite FK (Lab 1, VEHICLE)
```sql
CREATE TABLE vehicle
(plates varchar(6) PRIMARY KEY,
 year   integer,
 eng_no varchar(8) NOT NULL,
 ch_no  varchar(8) NOT NULL,
 type   char(1) CONSTRAINT check_type CHECK (type IN ('p','r','t','l','m')),
 make   varchar(10) NOT NULL,
 model  varchar(10) NOT NULL,
 FOREIGN KEY (make, model) REFERENCES vehicle_type);
```

PK made of two columns incl. a date (Lab 1, OWNS)
```sql
CREATE TABLE owns
(plates        varchar(6),
 ownerid       char(8) NOT NULL,
 purchase_date date NOT NULL,
 drr           integer,
 datesold      date,
 PRIMARY KEY (plates, purchase_date),
 FOREIGN KEY (ownerid) REFERENCES owner,
 FOREIGN KEY (plates) REFERENCES vehicle);
```

Named PK, CHECK on two columns (lecture lab test, ACCOUNT)
```sql
CREATE TABLE account
(acc_no      integer NOT NULL CHECK (acc_no > 0),
 type        varchar(7) NOT NULL CHECK (type IN ('savings','cheque')),
 branch      varchar(7) NOT NULL,
 customer    char(9) NOT NULL REFERENCES cust,
 open_date   date NOT NULL,
 status      varchar(7) NOT NULL CHECK (status IN ('active','closed','frozen')),
 closed_date date,
 CONSTRAINT pk_account PRIMARY KEY (acc_no),
 CONSTRAINT check_dates CHECK (closed_date > open_date));
```

CREATE TABLE AS with aggregate (Lab 4 Q2, OWNER2)
```sql
CREATE TABLE owner2 AS
SELECT dr_lic, lname, fname, COUNT(*) AS no_cars
FROM   owns JOIN owner ON ownerid = dr_lic
WHERE  datesold IS NULL
GROUP BY dr_lic, fname, lname;
```

Copy someone else's table (Lab 3/4)
```sql
CREATE TABLE employee AS SELECT * FROM tanja.employee;
```

## When a CHECK can't do it
Lecture lab test (ORDER_ITEM): `product_cost` must equal the product's cost × quantity — needs data from COMP table, so CHECK can't do it → BEFORE INSERT trigger (CHECK_PRICE) → see [[TRIGGERS]]
