Combine rows from several tables by matching a foreign key to a primary key. [[SELECT]] · [[AGGREGATES]] · [[Schemas]]

## Template
```sql
-- style 1: tables in FROM, join condition in WHERE
SELECT cols
FROM   table1, table2
WHERE  table1.fk = table2.pk
  AND  other_conditions;

-- style 2: JOIN ... ON
SELECT cols
FROM   table1 JOIN table2 ON table1.fk = table2.pk
WHERE  other_conditions;
```
Both give the same result — labs use both.

## Rules
- **n tables → n−1 join conditions.** Forgetting one gives every combination of rows (huge wrong result).
- Join FK to the PK it references — check [[Schemas]] for which column points where (e.g. `movie.director = director.dnumber`, `owns.ownerid = owner.dr_lic`).
- Column name in more than one table → prefix it: `vehicle.plates`, `director.fname`, `star.fname`.
- Table alias: write it after the table name (`registration R`), then use `R.plates`.
- **Same table twice (self join) → must use aliases** (`employee E, employee M`).
- Many-to-many goes through the linking table: STAR ↔ STARS ↔ MOVIE, VEHICLE ↔ OWNS ↔ OWNER.
- Joins can create duplicate rows → `DISTINCT` if you only want each name once.
- "Current owner" in REGISTRATION db = `datesold IS NULL` in OWNS.

## Examples (from labs)
Two tables (Lab 2 Q11) — every movie title with its director's name
```sql
SELECT title, fname, lname
FROM   movie, director
WHERE  director = dnumber;
```

Three tables through linking table (Lab 2 Q12) — star who played Vronsky in 'Anna Karenina'
```sql
SELECT fname, lname
FROM   star, stars, movie
WHERE  title = 'Anna Karenina' AND role = 'Vronsky'
  AND  movie = mnumber AND snumber = star;
```

Four tables + DISTINCT (Lab 3 Q1) — stars in movies directed by Sofia Coppola
```sql
SELECT DISTINCT star.fname, star.lname
FROM   star, stars, movie, director
WHERE  star = snumber AND movie = mnumber AND director = dnumber
  AND  director.fname = 'Sofia' AND director.lname = 'Coppola';
```

JOIN ... ON (Lab 2 Reg Q5) — each car with its current owner
```sql
SELECT plates, fname, lname
FROM   owner JOIN owns ON ownerid = dr_lic
WHERE  datesold IS NULL;
```

Join with a filter on the other table (Lab 2 Reg Q2) — cars imported from Japan
```sql
SELECT vehicle.plates, make, model
FROM   registration, vehicle
WHERE  registration.plates = vehicle.plates AND country = 'Japan';
```

Self join — same table twice (Lab 3 Reg Q2) — R1 finds the Japan import, R2 counts all its registrations
```sql
SELECT vehicle.plates, make, model, COUNT(*) AS no_regs
FROM   vehicle, registration R1, registration R2
WHERE  R1.plates = vehicle.plates AND R1.country = 'Japan'
  AND  R1.reg_date > '01-jan-85'
  AND  R1.plates = R2.plates
GROUP BY vehicle.plates, make, model
HAVING COUNT(*) < 3;
```

Self join — employee and their manager (Lab 4 Q3) — E = employees, M = manager
```sql
SELECT org_number, M.lname, M.fname, COUNT(*) AS total_emp
FROM   reg_org, employee E, employee M
WHERE  manager = M.ird AND E.reg_org = org_number
GROUP BY org_number, M.lname, M.fname;
```
