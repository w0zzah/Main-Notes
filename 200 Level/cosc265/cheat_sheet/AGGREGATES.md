COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING

Turn many rows into one value, either for the whole table or per group. [[SELECT]] · [[JOINS]] · [[Subqueries]] · [[VIEW]]

## Template
```sql
-- one value for the whole table
SELECT COUNT(*), SUM(col), AVG(col), MIN(col), MAX(col)
FROM   table
WHERE  condition;

-- one value per group
SELECT group_col1, group_col2, COUNT(*) AS name
FROM   table
WHERE  row_condition          -- filters rows BEFORE grouping
GROUP BY group_col1, group_col2
HAVING COUNT(*) > n           -- filters groups AFTER grouping
ORDER BY name DESC;
```

## The functions

| Function | Gives | Lab example |
|---|---|---|
| `COUNT(*)` | number of rows | Lab 3, Lab 4 |
| `SUM(col)` | total | Lab 2 Q10 |
| `AVG(col)` | average | — |
| `MIN(col)` | smallest | — |
| `MAX(col)` | largest | — |

## Rules
- Every column in SELECT that is **not** inside an aggregate **must be in GROUP BY**.
- Aggregates can't go in WHERE → put them in HAVING.
- WHERE = which rows go into the groups. HAVING = which groups come out.
- Group by the **key** as well as the name (`GROUP BY snumber, fname, lname`) otherwise two different people with the same name get merged into one group. The key doesn't have to be in SELECT.
- Give the aggregate an alias (`AS no_movies`) to use it in ORDER BY or as a column name in a view / CREATE TABLE AS.
- A view built with an aggregate or GROUP BY **can't be updated/deleted from** 

## Question patterns
| Question says                                 | Pattern                                                |
| --------------------------------------------- | ------------------------------------------------------ |
| "total / how many overall"                    | aggregate, no GROUP BY                                 |
| "for each X" / "per X"                        | GROUP BY X                                             |
| "at least two / more than one / fewer than 3" | GROUP BY + `HAVING COUNT(*) >= 2` / `> 1` / `< 3`      |
| "at least as many as X"                       | `HAVING COUNT(*) >= (subquery counting X)`             |
| "the most / the highest"                      | `HAVING COUNT(*) >= ALL (subquery with same GROUP BY)` |
| "order by number of"                          | `ORDER BY alias DESC`                                  |

## Examples (from labs)
SUM over filtered rows (Lab 2 Q10) — total awards won by comedies
```sql
SELECT SUM(aawon)
FROM   movie
WHERE  type = 'comedy';
```

GROUP BY + HAVING + ORDER BY (Lab 3 Q3) — movie types with more than 5 movies, most first
```sql
SELECT type, COUNT(*) AS no_movies
FROM   movie
GROUP BY type
HAVING COUNT(*) > 5
ORDER BY no_movies DESC;
```

Join + GROUP BY key + HAVING (Lab 3 Q2) — stars in at least two Sofia Coppola movies
```sql
SELECT star.fname, star.lname, COUNT(*)
FROM   star, stars, movie, director
WHERE  star = snumber AND movie = mnumber AND director = dnumber
  AND  director.fname = 'Sofia' AND director.lname = 'Coppola'
GROUP BY star.fname, star.lname, snumber
HAVING COUNT(*) >= 2;
```

"More than one" (Lab 3 Reg Q3) — people who currently own more than one vehicle
```sql
SELECT lname, init, fname
FROM   owner JOIN owns ON ownerid = dr_lic
WHERE  datesold IS NULL
GROUP BY dr_lic, lname, init, fname
HAVING 1 < COUNT(*);
```

"At least as many as X" (Lab 3 Q4) — directors with at least as many movies as director 15
```sql
SELECT fname, lname
FROM   director JOIN movie ON director = dnumber
GROUP BY director, fname, lname
HAVING COUNT(*) >= (SELECT COUNT(*) FROM movie WHERE director = 15);
```

"The most" (Lab 3 Q5) — director who directed the most dramas
```sql
SELECT fname, lname
FROM   director JOIN movie ON director = dnumber
WHERE  type = 'drama'
GROUP BY director, fname, lname
HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM movie
                        WHERE type = 'drama' GROUP BY director);
```

Aggregate inside a view (Lab 3 Q6) — times each vehicle registered, then query the view
```sql
CREATE VIEW veh_info AS
SELECT vehicle.plates, make, model, COUNT(*) AS regno
FROM   vehicle JOIN registration ON registration.plates = vehicle.plates
GROUP BY vehicle.plates, make, model;

SELECT plates FROM veh_info WHERE regno >= 3;
```
(lab solution writes `regno > 3`, but the question says "at least three" → `>= 3`)

Aggregate inside a trigger — count into a variable (Lab 4 Q2)
```sql
SELECT COUNT(*) INTO check_tuple
FROM   owner2
WHERE  dr_lic = :new.ownerid;
```
