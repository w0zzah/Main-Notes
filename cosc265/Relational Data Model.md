

## 1. Structural Components

### Relational Terminology

- **Relation:** A set of tuples (rows) and attributes (columns).
- **Domain:** A set of valid values permitted for a given attribute.
- **Relation Schema:** Defined as $R(A_1, A_2, \dots, A_n)$, where $R$ is the relation name and $A_i$ are the attributes.   
- **Relational Database Schema:** Defined as $S = \{R_1, R_2, \dots, R_n\}$, representing the set of relation schemas in the database.
- **Cardinality:** The total number of rows (tuples) in a relation.
- **Degree / Arity:** The total number of columns (attributes) in a relation.

### Formal vs. Informal Terms

| **Informal Term**  |         **Formal Term**         |
| :----------------: | :-----------------------------: |
|       Table        |            Relation             |
|       Column       |            Attribute            |
|        Row         |              Tuple              |
| Values in a Column |             Domain              |
|  Table Definition  |      Schema of a Relation       |
|  Populated Table   | Extension (State) of a Relation |

## 2. Integrity Constraints

**Constraints are conditions that must hold true for all valid relation states in the database.**

- **Domain Constraint:** Specifies that all values appearing in an attribute column must belong to the corresponding domain. 
- **Entity Integrity Constraint:** No primary key value can be `NULL`. Every tuple in a relation must be uniquely identifiable.
- **Referential Integrity Constraint:** Ensures consistency between two relations that maintain a reference link via foreign keys.

## 3. Keys & Relationships

### Key Definitions

- **Superkey:** Any set of attributes that uniquely identifies a tuple in a relation.
- **Candidate Key (Key):** A minimal superkey—a superkey from which no attribute can be removed without losing the uniqueness property.
- **Primary Key:** A designated candidate key chosen to uniquely identify tuples in a relation. Primary key values cannot be `NULL`.
### Referential Integrity (Foreign Keys)

A Foreign Key (FK) in a referencing relation points to a Primary Key (PK) in a referenced relation. The value of a foreign key must either be:
1. An existing primary key value in the referenced relation.
2. `NULL` (indicating no reference).

## Semantic Interity Constraints
- No. of hours per employee constraint spec lang may be req

### Phases of DB Design (Slides 3 pg 23)

### Step 1: Mapping of regular Entity Types
- For each strong entity type in the er schema create a relation r that includes all the simple attrs of E
- Chose one of the key attr as the primary key, if the chosen key is composite the set of simple attr that form it will together form the primary key of R
### Step 2: Mapping of weak entity types
- for each weak entity type W in the ER schema, with owner entity type e, create a relation r and include all simple attributes of W as attributes of r
- Include any foreign key attrs of R the primary key attr(s) of the relation that correspond to the owner entity types
### Step 3: Mapping of Binary 1:1 Relationship Types
- Identify the relations S and T that correspond to the entity types participating in R
- Choose one of the relations and include a foreign key in s the primary ket of T. It is better to choose an entity type with total participation in R
- Add attributes of the relationship type to the same relation

### Step 4: Mapping of Binary 1:N Relationship Types
- For each regular binary 1:N relationship type R, Identify the relation S that represent the participating entity type at the n-side of the relationship type
- Include as foreign key in S the primary key of the relation T that represent the other entity type participating in R
- Include any simple attributes of the 1:N relationship type as attributes of S

### Step 5: Mapping of Binary M:N Relationship Types
- For each regular binary M:N relationship type, create a new relation S to rep R
- Include as foreign key attributes in S the primary keys of the relations that represent the participating entity types; their combination will form the primary key of S
- Also include any simple attr of M:N relationship type

### Step 6: Mapping of Multivalued attributes
- For each multivalue attribute create a new relation R & inclyude amn attr corr to A
- The primary key of R is the combo of A n K if the multivalued attr is  composite, we include its simple components

### Step 7: Mapping of N-ary Relationship Types
- for each n-ary rel tρype R where n> 2 create a new rela S to rep R
- Include as foreign key attr in S the primary keys of the rels that rep participating entity types
- include any simp attr of n-ary rella types as attr of S

### Step 8: Options for Mapping Specialization/Generalization

When you have a type of entity such as a "Software" Engineer or a "Mechanical" Engineer, then you need to specify with a disjoint relationship. (Little circle with d in the middle.) Employee forms a relationship to "d" which splits into Mechanical and Software. You need to name the split by name and put a semi circle in the direction of the subclasses.


**Option A: superclass and sublasses (works for any specialization)**
- - Create a rel L for C with attr Attrs(L) = {k, a,...an} and PK(L) = k. Create a relation L for each subclass Si, 1 < l < m with the attrs  

**Option B: subclass relations only (only works for total specializations)**
- Create a relation L for each subclass 1 < i < m with the attributes Attr(Li) = {attributes of Si} U {k, a,...an} and PK(Li) = k

**Option 8C: Single relation with one type attribute**
- Create a single relation L with attributes Attrs(L) = {k,a1,…an} U {attributes of S1} U…U {attributes of Sm} U {t} and PK(L) = k. The attribute t is called a type (or discriminating) attribute that indicates the subclass to which each tuple belongs

**Option 8D: Single relation with multiple type attributes** 
- Create a single relation schema L with attributes Attrs(L) = {k,a1,…an} U {attributes of S1} U…U {attributes of Sm} U {t1, t2,…,tm} and PK(L) = k. Each ti, 1 < I < m, is a Boolean type attribute indicating whether a tuple belongs to the subclass Si.

### STEP 9: MAPPING OF CATEGORIES
- Create a new relation for each category and specify the key, or **surrogate key**


### Update Operation's:
- **Insert | Delete | Modify**
- Must not break the integrity constraints:
	- Cancel operation that causes the violation (REJECT
	- Perform the operation but inform the user of violation
	- Trigger additional update so the violation is correced (CASCADE & SET NULL)


### Relational Algebra (Check Slides 3 pg 80)
- **Operations over relations:** (Unary(select, Project)) & **Binary**
	- Unary: Select, Project
	- Binary: Join, Division
- **Set operations**
	- Union, Intersection, Set difference, Cartesian product
- **Additional operations**
	- Outer joins
	- Grouping
	- Aggregate functions


**Select (σ):** "Getting on some tuples from the table"
- Unary, selection condition can be:
	- simple:  attr operation value
	- composite: simple conditions connected by "AND" "OR" and "Not"


**Project (π):** "List all of x,y,z"
- Unary
	- simple: pi ac
	- Composite pi ac(R)

#### **Set Operations:**

**Uninion (∪):** 

**Intersection (∩):** 

**Caretesian Product (x):**

**Join (><):** "Pick out 'x' from 'A' n 'B' -> for row Ax.. match to row Bx..."
- R.A = S.B
- Equijoin
- Theta join
- Natural join R*S



**Division:** "For R(A, B), find all R(B) that is related to S(A)"
- Given two relations R(X) and S(Z)
- R / S = T(Y) 
- Y = X-z
	For a tuple t to appear in T, the values in t must appear in R in combimnation with every tuplr in S


### Aggregate Functuions 

**Opertate on a set of tuples
- Sum
- Average
- Max
- Min
- Count
Use of the functional operator F

e.g F(supercript Max..)


### Grouping Functions
**Retrieve each directors number of movies they directed**
- grouping attr F flist (relatiation)
- DNO F counts ssn Average Salary


Left outer join right outer join Full outer join


### Strategy for Building queries

- Determine which  tables contain the data 
- Specify join conditions if there is more than one table in found in step 1 
- Specify selection conditions
- Specify expressions to appear in the result
- Group the tuples (if necessary)


### Views
- Virtual tables: data does not exist on the disk; instead the query is stored
- We do it this way for security by exporting the data, it also alows us to customise access to the data and the specifications of complex operations on base tables
- Updatable views is defined over a single table and contains a primary key. It does not invlve any aggregate functions or group