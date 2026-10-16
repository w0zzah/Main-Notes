Oracle errors you're likely to hit, what they mean and the fix. [[CREATE TABLE]] · [[INSERT]] · [[VIEW]] · [[TRIGGERS]] · [[AGGREGATES]]

## Creating / dropping
| Error | Meaning | Fix |
|---|---|---|
| ORA-00955 | name is already used by an existing object | `DROP TABLE name;` first, or use `CREATE OR REPLACE` (views, triggers) |
| ORA-00942 | table or view does not exist | check spelling / prefix (`tanja.movie`). Harmless on DROP lines the first time a script runs |
| ORA-02270 | no matching unique or primary key for this column-list | FK must point at a PK or UNIQUE column → add the PK to the parent first |
| ORA-02449 | unique/primary keys in table referenced by foreign keys | `DROP TABLE name CASCADE CONSTRAINTS;` |
| "created with compilation errors" | trigger/procedure has a PL/SQL error | `SHOW ERRORS;` |

## Inserting / updating / deleting
| Error | Meaning | Fix |
|---|---|---|
| ORA-00001 | unique constraint violated | row has the same PK/UNIQUE value as an existing row |
| ORA-01400 | cannot insert NULL | a NOT NULL column was left out or given null |
| ORA-02290 | check constraint violated | value breaks a CHECK (e.g. type not in the IN list) |
| ORA-02291 | integrity constraint violated – parent key not found | FK value doesn't exist in the parent table → insert the parent row first |
| ORA-02292 | integrity constraint violated – child record found | can't delete a parent row something still references → delete children first, or ON DELETE CASCADE |
| ORA-00947 / ORA-00913 | not enough / too many values | INSERT values don't match the column count → check `describe table;` |

## Queries
| Error | Meaning | Fix |
|---|---|---|
| ORA-00979 | not a GROUP BY expression | a SELECT column isn't in an aggregate or in GROUP BY |
| ORA-00934 | group function is not allowed here | aggregate in WHERE → move it to HAVING |
| ORA-00918 | column ambiguously defined | column is in two tables → prefix it (`vehicle.plates`) |
| ORA-01427 | single-row subquery returns more than one row | `= (subquery)` got several rows → use `IN` |

## Views / triggers
| Error | Meaning | Fix |
|---|---|---|
| ORA-01732 | data manipulation operation not legal on this view | aggregate / GROUP BY / DISTINCT view → INSTEAD OF trigger |
| ORA-01779 | cannot modify a column which maps to a non key-preserved table | join view → INSTEAD OF trigger |
| ORA-01403 | no data found | `SELECT ... INTO` in a trigger matched no rows → check with `COUNT(*) INTO` first |
| ORA-04091 | table is mutating | trigger reads/changes the table it's on |
| ORA-20000 to -20999 | your own `RAISE_APPLICATION_ERROR` | working as intended |
