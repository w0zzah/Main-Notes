Changes values in rows that **already exist**.  [[INSERT]] · [[DELETE]] · [[VIEW]] · [[Subqueries]]

## Template

```sql
UPDATE table_name
SET    col1 = expression [, col2 = expression ...]
WHERE condition;
```

## Rules

- Only **one table** per UPDATE statement. To change data in another table, use a subquery in WHERE or a separate UPDATE.
- **No WHERE = every row is changed.**
- The right-hand side can use the column's old value (`bonus = bonus + 5`).
- Text and dates go in single quotes: `'Simmons'`, `'01-jul-2011'`.
- Apostrophe inside a string → double it: `'O''Toole'`.
- `WHERE col = (subquery)` needs the subquery to return **one value**. If it could return several, use `IN (subquery)`.
- `ON UPDATE CASCADE` on a foreign key would push key changes to child tables — but **Oracle doesn't support ON UPDATE CASCADE** (only `ON DELETE CASCADE` / `ON DELETE SET NULL`).

## Updating through a view

> [!Important] When can you UPDATE a view? **Standard SQL**
> 
> - One underlying table and the view includes that table's primary key (or a candidate key)
> -  You **CANT** update views built on **multiple tables** (joins) — generally not updatable
> - You **CANT** update views using `GROUP BY`, aggregates (`COUNT`, `SUM`…), `DISTINCT`, `IN`, `ANY`, `ALL`, `EXISTS`
> 
> **Oracle**
> 
> - Single table views without aggregates / GROUP BY / set ops / DISTINCT are updatable **even without the PK** 
> - Some multi-table views are updatable if they contain a table's PK. Check which columns, check example from lab3 q4 below
> 
> ```sql
> SELECT column_name, updatable
> FROM   user_updatable_columns
> WHERE  table_name = UPPER('view_name');
> ```
> 
> **Fix for a non-updatable view:** write an `INSTEAD OF` trigger (Lab 4 Q3) → see [[TRIGGERS]]




## Examples (from lectures / labs)

**Change every row** (no WHERE) — increase each customer's bonus by 5

```sql
UPDATE customer
SET    bonus = bonus + 5;
```

**Change one row** — rename customer 303

```sql
UPDATE customer
SET    lname = 'Simmons'
WHERE  cnumber = 303;
```

**Change several columns at once** — movie 503

```sql
UPDATE movie
SET    aawon = 3, critics = '4'
WHERE  mnumber = 503;
```

**WHERE uses a subquery** (Lab 3 Q4a) — Anna Simmons painted her VW Golf green

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


## Updating via a trigger

- Inside a trigger body, refer to the row being changed with `:new.col` / `:old.col`.
- Derived columns (e.g. a total) can be kept correct with `AFTER UPDATE OF col ON table` triggers:

```sql
CREATE TRIGGER totalsal2
AFTER UPDATE OF salary ON employee
FOR EACH ROW
WHEN (new.dno IS NOT NULL)     -- no colon in WHEN
UPDATE department
SET    total_sal = total_sal + :new.salary - :old.salary
WHERE  dno = :new.dno;
/
```

