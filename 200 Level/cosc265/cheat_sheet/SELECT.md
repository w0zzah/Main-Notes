Retrieves data. Clause order below is the order you must write them. [[JOINS]] · [[AGGREGATES]] · [[Subqueries]] · [[Schemas]]

## Template
```sql
SELECT [DISTINCT] col1, col2, expression [AS alias] | *
FROM   table1 [alias], table2 [alias]
WHERE  condition
GROUP BY col1, col2
HAVING group_condition
ORDER BY col1 [DESC], col2 [ASC];
```
GROUP BY / HAVING → see [[AGGREGATES]]

## WHERE predicates (lecture)
```sql
WHERE born >= 1950                       -- comparisons: = <> != < <= > >=
WHERE year BETWEEN 1965 AND 1975         -- inclusive both ends
WHERE type = 'fantasy' OR type = 'romance'
WHERE type IN ('p','r','t')              -- IN list (or IN subquery)
WHERE died IS NULL                       -- NOT "= null"
WHERE died IS NOT NULL
WHERE lname LIKE 'S%'                    -- pattern match
WHERE EXISTS (subquery) / col >= ALL (subquery) / col = ANY (subquery)
```

|Operator|Meaning|Example|
|---|---|---|
|`=`|equal to|`snumber = 4`|
|`<>`|not equal to|`type <> 'comedy'`|
|`!=`|not equal to (same as `<>`)|`type != 'comedy'`|
|`<`|less than|`born < 1950`|
|`<=`|less than or equal to|`year <= 1975`|
|`>`|greater than|`died > 1930`|
|`>=`|greater than or equal to|`born >= 1950`|



## Rules
- `DISTINCT` removes duplicate rows — SQL results can contain duplicates otherwise (tables are multisets).
- Test for NULL with `IS NULL` / `IS NOT NULL`, never `= null`.
- `BETWEEN a AND b` includes a and b.
- Date ranges work with BETWEEN on date strings: `reg_date BETWEEN '01-jul-2011' AND '31-jul-2011'`
- Arithmetic in SELECT is allowed: `died - born` (Lab 2 Q9). Give it a name with `AS`.
- `ORDER BY` default is ascending. `DESC` applies only to the column it's written after.
- You can ORDER BY an alias from the SELECT (`ORDER BY no_movies DESC`).
- Text in single quotes; text comparisons are case sensitive (`'Sofia'` ≠ `'sofia'`), keywords/names aren't.
- String concatenation: `||`
- If a column name exists in two tables in FROM, prefix it: `vehicle.plates`, `star.fname`.

## Functions listed in lecture
- Aggregate: `sum, count, max, min, avg` → [[AGGREGATES]]
- Conversion: `to_char, to_date, to_number`
- Numeric: `abs, ceil, floor, mod, power, round, sqrt`
- String: `upper, lower, length, substr, instr`
- Date: `sysdate, add_months, months_between`
- Other: `nvl, decode, case`

## Examples (from labs)
All distinct values of a column (Lab 2 Q1)
```sql
SELECT DISTINCT type FROM movie;
```

Everything about one row (Lab 2 Q2)
```sql
SELECT * FROM star WHERE snumber = 4;
```

Range (Lab 2 Q5)
```sql
SELECT mnumber, title
FROM   movie
WHERE  year BETWEEN 1965 AND 1975;
```

OR (Lab 2 Q6)
```sql
SELECT mnumber, title
FROM   movie
WHERE  type = 'fantasy' OR type = 'romance';
```

Range + IS NULL — born in 1920s and still living (Lab 2 Q7)
```sql
SELECT fname, lname, born, city
FROM   star
WHERE  born BETWEEN 1920 AND 1929 AND died IS NULL;
```

Calculated column (Lab 2 Q9) — how long deceased directors lived
```sql
SELECT fname, lname, died - born
FROM   director
WHERE  died IS NOT NULL;
```

ORDER BY two columns, different directions (Lab 2 Reg Q4)
```sql
SELECT fname, lname
FROM   owner
ORDER BY lname DESC, fname;
```

Date range (Lab 3 Reg Q1) — vehicles registered in July 2011
```sql
SELECT *
FROM   vehicle JOIN registration R ON R.plates = vehicle.plates
WHERE  reg_date BETWEEN '01-jul-2011' AND '31-jul-2011';
```

## Relational algebra (Lab 2)
| Symbol          | Meaning         | SQL                       |
| --------------- | --------------- | ------------------------- |
| σ condition (R) | select rows     | WHERE                     |
| π cols (R)      | project columns | SELECT cols (DISTINCT)    |
| R ⋈ cond S      | join            | JOIN ... ON / WHERE a = b |
| ℱ SUM col (R)   | aggregate       | SUM(col)                  |

e.g. Lab 2 Q7: `π Fname,Lname,Born,City (σ Born>=1920 AND Born<=1929 AND Died=NULL (STAR))`
