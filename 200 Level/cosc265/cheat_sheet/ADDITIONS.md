# Additions from the marina practice test

Each section says which of your files it goes in. Marina tables used below:
- BOAT_OWNER (**ownerno**, fname, lname, address)
- BOAT (**name**, model, length, owner → boat_owner)
- BERTH (**berthno, marina**, type, length, boat → boat)
- PRICES (marina, type, amount_year …)
- SERVICE (**type**, description)

---

## → JOINS.md

### Rules (add)
- **Outer join** keeps rows that have no match. Use it when the question says "include X *if* …" / "show all X, and Y where there is one". An inner join would drop the unmatched rows.
- `LEFT OUTER JOIN` keeps every row of the **left** table. The missing columns from the right table come back NULL.
- Join on **two columns** when the key is composite: `ON p.marina = b.marina AND p.type = b.type`.
- JOINs can be chained: `A JOIN B ON ... JOIN C ON ...`

### Examples (add)
LEFT OUTER JOIN (practice test Q8, BERTH8). All 8 m berths, plus the boat and owner if the berth is occupied:
```sql
CREATE OR REPLACE VIEW berth8 AS
SELECT berthno, marina, type, boat, fname, lname
FROM   berth LEFT OUTER JOIN (boat_owner JOIN boat ON owner = ownerno)
       ON boat = name
WHERE  berth.length = 8;
```
Empty berths still show, with blank boat/fname/lname.

Two-column join + chained JOIN + calculated column (practice test Q4). Yearly price for Fish 'N Ships:
```sql
SELECT amount_year * boat.length AS yearly_price
FROM   prices p JOIN berth b ON p.marina = b.marina AND p.type = b.type
                JOIN boat     ON boat.name = b.boat
WHERE  b.marina = 1 AND b.type = 'wharf' AND boat = 'Fish ''N Ships';
```

---

## → INSERT.md

### Rules (add)
- INSERT … SELECT can mix **literal values** with columns looked up from another table. Use this when you know the name but not the key (e.g. owner number).
- The lookup's WHERE must find exactly one row, or you insert several rows / none. Use first **and** last name.

### Examples (add)
Literal values + looked-up FK (practice test Q3). Philomena Blake registers "Fish 'N Ships", Rayglass 3500, 12 m:
```sql
INSERT INTO boat
SELECT 'Fish ''N Ships', 'Rayglass 3500', 12, ownerno
FROM   boat_owner
WHERE  fname = 'Philomena' AND lname = 'Blake';
```
No VALUES keyword. Column order = BOAT's CREATE TABLE order (name, model, length, owner).

---

## → UPDATE.md

### Examples (add)
Pick the first free slot with MIN in a subquery (practice test Q4). Dock Fish 'N Ships at the first empty wharf berth in marina 1:
```sql
UPDATE berth
SET    boat = 'Fish ''N Ships'
WHERE  marina = 1
  AND  berthno = (SELECT MIN(berthno)
                  FROM   berth
                  WHERE  marina = 1 AND type = 'wharf' AND boat IS NULL);
```
Two-step version (also accepted): `SELECT * FROM berth WHERE marina = 1 AND type = 'wharf';` to find an empty one, then UPDATE that berthno.

Updating a view with an outer join fails (practice test Q9):
```sql
UPDATE berth8
SET    boat = 'Sea-Batical', fname = 'Peter', lname = 'Norton'
WHERE  marina = 3 AND berthno = 4;
-- fails: view is not updatable → INSTEAD OF trigger (see TRIGGERS)
```

---

## → SELECT.md

### WHERE predicates (add under LIKE)
```sql
WHERE address LIKE '%Ilam%'     -- % = any number of characters (incl. none)
WHERE lname   LIKE 'Sm_th'      -- _ = exactly one character
WHERE service IN (SELECT type FROM service
                  WHERE description LIKE '%engine%')   -- IN with a subquery
```

### Rules (add)
- Comparing anything to NULL gives **UNKNOWN** (not true, not false). WHERE only keeps rows that are TRUE, so `col = null` returns nothing → use `IS NULL`.

### Examples (add)
Several tables + IN subquery + LIKE (practice test Q7). New engine requests in marina 1 under 5 hours, with boat model and owner:
```sql
SELECT rid, model, fname, lname
FROM   request, boat_owner, boat
WHERE  owner = ownerno AND boat.name = request.boat
  AND  request.marina = 1
  AND  service IN (SELECT type FROM service WHERE description LIKE '%engine%')
  AND  est_hours < 5 AND status = 'n';
```

---

## → AGGREGATES.md

### Examples (add)
"Two or more of the same X" (practice test Q2). Owners with 2+ boats of the same model:
```sql
SELECT fname, lname, COUNT(*), model
FROM   boat_owner JOIN boat ON owner = ownerno
GROUP BY ownerno, fname, lname, model
HAVING COUNT(*) >= 2;
```
"Of the same model" → model goes in GROUP BY.

"The most", same pattern as Lab 3 Q5 (practice test Q11). Owner with the most boats:
```sql
SELECT fname, lname, COUNT(*)
FROM   boat JOIN boat_owner ON owner = ownerno
GROUP BY owner, fname, lname
HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM boat GROUP BY owner);
```

---

## → TRIGGERS.md

### Choosing the type (add a row)
| Need | Use |
|---|---|
| Update a non-updatable view **and check the data first** | `INSTEAD OF` + `COUNT(*) INTO` checks + `IF/ELSIF` + `RAISE_APPLICATION_ERROR` |

### Validation pattern
1. One `SELECT COUNT(*) INTO var` per thing to check (0 = doesn't exist / isn't true)
2. `IF var = 0 THEN RAISE_APPLICATION_ERROR(...)` for each check, in an `ELSIF` chain
3. Only in the final `ELSE` do the real change on the base table

### Examples (add)
INSTEAD OF with validation (practice test Q10, ADD_BOAT on BERTH8)
```sql
CREATE OR REPLACE TRIGGER add_boat
INSTEAD OF UPDATE ON berth8
FOR EACH ROW
DECLARE
    found_owner   integer;
    found_boat    integer;
    owner_correct integer;
    berth_empty   integer;
    boat_length   float;
    berth_length  float;
BEGIN
    -- owner exists?
    SELECT COUNT(*) INTO found_owner
    FROM   boat_owner
    WHERE  lname = :new.lname AND fname = :new.fname;

    -- boat exists?
    SELECT COUNT(*) INTO found_boat
    FROM   boat
    WHERE  name = :new.boat;

    -- this owner owns this boat?
    SELECT COUNT(*) INTO owner_correct
    FROM   boat JOIN boat_owner ON ownerno = owner
    WHERE  name = :new.boat AND fname = :new.fname AND lname = :new.lname;

    -- berth empty?
    SELECT COUNT(*) INTO berth_empty
    FROM   berth
    WHERE  berthno = :new.berthno AND marina = :new.marina AND boat IS NULL;

    IF found_owner = 0 THEN
        RAISE_APPLICATION_ERROR(-20100, 'There is no owner with the given name!');
    ELSIF found_boat = 0 THEN
        RAISE_APPLICATION_ERROR(-20101, 'There is no boat with that name!');
    ELSIF owner_correct = 0 THEN
        RAISE_APPLICATION_ERROR(-20101, 'The boat is not owned by the specified person!');
    ELSIF berth_empty = 0 THEN
        RAISE_APPLICATION_ERROR(-20101, 'The specified berth is already taken!');
    ELSE
        SELECT length INTO boat_length
        FROM   boat
        WHERE  name = :new.boat;

        SELECT length INTO berth_length
        FROM   berth
        WHERE  marina = :new.marina AND berthno = :new.berthno;

        IF boat_length > berth_length THEN
            RAISE_APPLICATION_ERROR(-20102, 'The boat is too long for the berth!');
        ELSE
            UPDATE berth
            SET    boat = :new.boat
            WHERE  berthno = :new.berthno AND marina = :new.marina;
        END IF;
    END IF;
END;
/
```
- Checks use `COUNT(*) INTO` because COUNT always returns one row. A plain `SELECT length INTO` with no match would error, so it only runs after the checks pass.
- Test it by re-running the Q9 UPDATE. Sea-Batical is too long for berth 4 → `ORA-20102: The boat is too long for the berth!`
- The solution writes `raise_application_error(num=>-20100, msg=>'...')`. The named form means the same thing.
