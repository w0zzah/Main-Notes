Removes rows from a table (the table itself stays). [[INSERT]] · [[Update]] · [[VIEW]] · [[ALTER-DROP]]

## Template
```sql
DELETE FROM table_name
WHERE  condition;
```

## Rules
- No WHERE = **every row is deleted**, table becomes empty (but still exists — unlike DROP TABLE).
- Deletes from **one table at a time** (unless an FK has `ON DELETE CASCADE`, which also deletes the child rows).
- Can't delete a row that other rows still reference through an FK (referential integrity) — unless the FK has `ON DELETE CASCADE` / `ON DELETE SET NULL`.
- WHERE can use a subquery, same as [[Update]] → see [[Subqueries]].
- Handy before re-running an insert script: `DELETE FROM table_name;` at the top (Lab 1).

## Deleting through a view
Same rules as updating a view → see [[VIEW]] / [[Update]]
- You CANT delete from a view defined with an aggregate / GROUP BY (Lab 3 Q6, `veh_info` — error)

## Examples (from lectures / labs)
Delete one row (lecture Ex 4) — customer 127
```sql
DELETE FROM customer
WHERE  cnumber = 127;
```

Delete everything in a table (lecture Ex 5) — contents of STARS
```sql
DELETE FROM stars;
```

Delete several rows matching a condition (Lab 3 Q4c) — all registrations for TX9283
```sql
DELETE FROM registration
WHERE  plates = 'TX9283';
```

Delete on an aggregate view — fails (Lab 3 Q6)
```sql
DELETE FROM veh_info
WHERE  plates = 'FO2341';
-- error: view is defined with COUNT(*) / GROUP BY, so not updatable
```

## Deleting via a trigger
Use `:old.col` for the row being deleted (lecture, keeps department total correct):
```sql
CREATE TRIGGER totalsal3
AFTER DELETE ON employee
FOR EACH ROW
WHEN (old.dno IS NOT NULL)
UPDATE department
SET    total_sal = total_sal - :old.salary
WHERE  dno = :old.dno;
/
```
