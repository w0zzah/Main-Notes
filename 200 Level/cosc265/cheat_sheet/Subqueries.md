# Subqueries

A SELECT inside another statement, in brackets. [[SELECT]] · [[AGGREGATES]] · [[Update]] · [[INSERT]]

## Template
```sql
WHERE  col =   (SELECT one_col FROM ... WHERE ...)   -- must return ONE value
WHERE  col IN  (SELECT one_col FROM ...)             -- any number of values
HAVING COUNT(*) >= (SELECT COUNT(*) FROM ...)        -- compare to one number
HAVING COUNT(*) >= ALL (SELECT COUNT(*) ... GROUP BY ...)  -- bigger than/equal to every value
WHERE  col = ANY (SELECT ...)                        -- matches at least one value
WHERE  EXISTS (SELECT * FROM ... WHERE ...)          -- true if subquery returns any row
WHERE  NOT EXISTS (SELECT ...)
```

## Where they can go
| Place | Example |
|---|---|
| WHERE of SELECT / UPDATE / DELETE | Lab 3 Q4a |
| HAVING | Lab 3 Q4, Q5 |
| INSERT INTO ... SELECT | [[INSERT]] |
| CREATE TABLE ... AS SELECT | [[CREATE TABLE]] |
| CREATE VIEW ... AS SELECT | [[VIEW]] |
| CHECK constraint | **NOT in Oracle** → use a [[TRIGGERS\|trigger]] |

## Rules
- Subquery returns one column.
- `=`, `>`, `>=` etc. with a plain subquery → it must return exactly **one** row, otherwise error. If it might return several → `IN`, or `ALL` / `ANY`.
- `>= ALL (...)` is the "the most" pattern; the subquery needs the same grouping as the outer query.
- Views using `IN`, `ANY`, `ALL`, `EXISTS` aren't updatable (standard SQL) → see [[VIEW]]
- Inside PL/SQL (triggers) a SELECT must put its result somewhere: `SELECT ... INTO variable` → see [[TRIGGERS]]

## Examples (from lectures / labs)
Single value in UPDATE's WHERE (Lab 3 Q4a) — Anna Simmons' VW Golf painted green
```sql
UPDATE color
SET    color = 'green'
WHERE  plates = (SELECT owns.plates
                 FROM   owns, owner, vehicle
                 WHERE  owns.plates = vehicle.plates
                   AND  ownerid = dr_lic
                   AND  lname = 'Simmons' AND fname = 'Anna'
                   AND  make = 'VW' AND model = 'golf');
```

Compare to one number in HAVING (Lab 3 Q4)
```sql
HAVING COUNT(*) >= (SELECT COUNT(*) FROM movie WHERE director = 15);
```

ALL — "the most" (Lab 3 Q5)
```sql
HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM movie
                        WHERE type = 'drama' GROUP BY director);
```

NOT EXISTS — "no row breaks the rule" (lecture, assertion; assertions not in Oracle)
```sql
CREATE ASSERTION salary_constraint
CHECK (NOT EXISTS
        (SELECT *
         FROM   employee e, employee m, department d
         WHERE  e.salary > m.salary
           AND  e.dno = d.dnumber
           AND  d.mgrssn = m.ssn));
```
