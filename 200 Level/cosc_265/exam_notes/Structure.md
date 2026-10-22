# COSC265 Exam Study Plan


## Priority overview


|     | Section                                           | Questions        | Marks | Your status            |
| --- | ------------------------------------------------- | ---------------- | ----- | ---------------------- |
| 1   | Conceptual modelling and EER to relational        | Q1, Q2, Q7b-d    | 21    | Attempted, with errors |
| 2   | Relational model, keys, integrity, views          | Q4, Q7a, Q7e, Q8 | 19    | Q8 blank               |
| 3   | Normalization, FDs, anomalies                     | Q3, Q9           | 20    | Blank                  |
| 4   | Relational algebra and SQL                        | Q5, Q6           | 10    | Attempted              |
| 5   | Indexing and physical storage                     | Q10-Q13          | 13    | Blank                  |
| 6   | Query optimization, transactions, denormalization | Q14-Q19          | 17    | Blank                  |

## Section 1: Conceptual modelling and EER to relational (21 marks)

**Exam content**

- Q1, Q2: map the EER to relations. Official answer has PERSON with Region, Client and Consultant; Region; ClientServices(Client, Service); ConsultantSpecialization(Consultant, Specialization); Contract; ContractBetween(Contract, Client, Consultant); ContractedServices(Contract, Client, Consultant, Service).
- Q7b-d: disjoint vs overlapping specialization, total vs partial category, conceptual vs logical design.

**What to learn**

- Reading (min,max) pairs: what the min and max each mean, and which side of the relationship line the pair describes.
- The mapping algorithm: each multivalued attribute becomes its own relation with a composite key. Your Q2 answer put NeededService, Specialization and Service in a single column, which breaks 1NF.
- Why a relationship with its own multivalued attribute (HAS, with Service) needs a separate relation including the keys of all participants.
- Specialization mapping options and when each fits.

**Guiding questions**

- Why is (1,1) correct for PERSON in LOCATED_IN, when the spec says a contract usually involves the same region but not always?
- If a consultant has three specializations, what would your Q2 schema do to the Consultant row?

## Section 2: Relational model, keys, integrity, views (19 marks)

**Exam content**

- Q4: keys. EMPLOYEE has PK Emp_No. PILOT has PK EmpNo, which is also an FK. FLIGHT has PK FlightNo and FKs Pilot and Copilot.
- Q7a: key vs superkey (minimality). Q7e: views (stored SELECT in the catalog) vs base tables (physically stored).
- Q8: the four integrity constraints: domain, key, entity integrity, referential integrity, plus how each is expressed in SQL.

**What to learn**

- Superkey, candidate key, primary key, foreign key, and nullable foreign keys (Copilot).
- For each of the four constraints: a definition, a one-line violation example, and the SQL keyword (data types and CHECK, PRIMARY KEY and UNIQUE, NOT NULL, FOREIGN KEY ... REFERENCES with ON DELETE/UPDATE actions).
- Views: when the query runs, what the catalog stores, and one reason to use a view.

**Guiding questions**

- Why can Pilot.EmpNo be both a primary key and a foreign key?
- What happens to FLIGHT rows if a PILOT row is deleted, under each referential action?

## Section 3: Normalization, FDs, anomalies (20 marks)

**Exam content**

- Q3: why one Excel sheet is worse than a database. The model answer covers security and backup, input checking, concurrent access, redundancy, and insertion, deletion and modification anomalies with concrete examples, plus multivalued cells.
- Q9: minimal cover of F = {AB->C, DEG->H, A->B, DG->H}. Answer: {A->B, A->C, DG->H}.

**What to learn**

- The three anomaly types, each with an example drawn from the scenario (for example: deleting a client's last contract loses the client; adding a specialization means editing many rows).
- Minimal cover procedure: (1) one attribute on each right side, (2) remove extraneous left-side attributes using closures, (3) remove redundant FDs.
- Attribute closure, which is the core skill under everything else here.
- Normal forms 1NF to BCNF and why multivalued cells violate 1NF.

**Guiding questions**

- In AB->C, why is B extraneous once you know A->B?
- In DEG->H, which attribute can you drop, and what does DG->H tell you?

## Section 4: Relational algebra and SQL (10 marks)

**Exam content**

- Q5: flights flown by 105 but not involving 109. The model SQL uses NOT EXISTS on a self-reference; the algebra alternative is a set difference of two projected selections.
- Q6: (a) the pilot employee numbers in Flight; (b) names, hire dates and certificate data for the copilot of flight 1003; (c) a count of flights per pilot.

**What to learn**

- Selection, projection, join (theta and natural), set difference, aggregate operator syntax.
- Writing "X but not Y" with set difference or NOT EXISTS, and why NULL Copilot values make a plain `<>` test unsafe.
- Reading a multi-join expression from the inside out and evaluating it by hand against the sample tables.

**Guiding questions**

- For flight 1003, what does each join in Q6b narrow down, step by step?
- Why must both Pilot and Copilot columns appear in each condition of Q5?

## Section 5: Indexing and physical storage (13 marks)

**Exam content**

- Q10: only one clustered index per table.
- Q11: log2(250,000) block reads (index of 100M entries at 20 B each in 8 KB blocks).
- Q12: dense (one entry per row), sparse (one per block), primary (on the sort column), secondary (not on the sort column).
- Q13: sparse two-level index trace for WGA and HAV gives blocks A, B, D, F, K.

**What to learn**

- Blocking factor and block counts: entries per block, then total blocks, then log2 for binary search.
- Dense vs sparse, primary vs secondary, and why a table can be physically sorted only once.
- The trace procedure: top level, then the last entry whose key is at most the search key, then bottom level, then data block. Repeat for each OR branch and union the blocks.

**Guiding questions**

- In Q11, which structure are you binary-searching, and why does that fix the number 250,000?
- Why does a sparse index only work on the ordering field?

## Section 6: Query optimization, transactions, denormalization (17 marks)

**Exam content**

- Q14: Dirty Read. Q15: Nonrepeatable Read. Q16: Phantom Read.
- Q17: indexing, sorting and hashing are all optimization methods.
- Q18: False, denormalization does not always improve performance.
- Q19: least efficient tree B, most efficient D, and an index on Student(Name) has no effect.

**What to learn**

- Anomaly definitions: reading uncommitted data (dirty), re-reading a row and getting a different value (nonrepeatable), and a re-run query returning a different set of rows (phantom). Practise telling them apart from the timeline.
- Heuristic optimization: push selections as far down the tree as possible, before joins. Compare trees by intermediate result size.
- When an index helps: only if the query filters or joins on the indexed column.
- Denormalization trade-offs: faster reads against redundancy and update cost.

**Guiding questions**

- In Q16, what changed between T1's reads: an existing row's value or the set of rows?
- Why does tree D beat tree A and tree C, and not only tree B?

## Weekly structure

1. **Days 1-2:** Section 3 (anomalies and minimal cover).
2. **Days 3-4:** Section 5 (indexing calculations and traces).
3. **Days 5-6:** Section 6 (transactions and optimization).
4. **Days 7-8:** Section 1 (redo Q1 and Q2 from scratch).
5. **Day 9:** Section 2 (integrity constraints in SQL).
6. **Day 10:** Section 4 (rewrite Q5 and Q6 without looking).
7. **Day 11:** timed 2-hour attempt at the full paper, then self-mark against the solutions.
8. **Day 12:** redo only the questions that lost marks.

The day counts are a guess because I don't know your exam date. If you tell me, I can compress or stretch this plan, and I can walk you through any section Socratically.