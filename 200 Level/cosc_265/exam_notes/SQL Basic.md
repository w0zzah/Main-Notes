ll 

### 1. Keys
- **Superkey.** A set of attributes whose values are unique accross all tuples.
- **Candidate key:** A minimal superkey, remove any attribute and uniquenesss is lost. 
- **Primary key:** The one candidate key the designer picks to identify tuples. The others are *alternate keys* and get the unique trait
- **Foreign key:** One or more attributes in a table whose values must match a key of another table or be nyll.

### 2. Constraints
- **Domain:** Every value must come from the attributes domain, e.g (all doctors need type 1 or 2 medical certificates)
```sql
Medical_Certificate INT CHECK (Medical_Certificate IN (1, 2))
Licence CHAR(3) CHECK (Licence IN ('ATP', 'COM'))
COL_1 TYPE CHECK (COL_1 in (constraint1, constraint2))
```
- **Key Constraint:** No two tuples may have the same value on a key
 ```sql
 Emp_No INT PRIMARY KEY,
 Email VARCHAR(100) UNIQUE
 ```

- **Referential Integrity:** A foregin key value must either match an existing value of the referenced key or be null

```sql
CREATE TABLE Flight (
  FlightNo INT PRIMARY KEY,
  Pilot    INT NOT NULL,
  Copilot  INT,
  FOREIGN KEY (Pilot)   REFERENCES Pilot(EmpNo)
      ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (Copilot) REFERENCES Pilot(EmpNo)
      ON DELETE SET NULL
);
```

### Core guidlines on tuples
- **Two entities share "identifiers" not attributes**
	- If two identities have a relationship, their only shared attributes should be the foreign key.
	- This is to lower coupling between the tables, as updating an entry of one can have a unimplied effect on the the other

- **Design relations so that no update anomilies are present**

- **Relations should be designed such that their typles will have as few NULL values as possible**
	- If the attribute is NULL frequently, they could be placed in seperate relations with the primary key

- **Spurious Tuples, Should satisfy a lossless join**
	- Bad designs for a relational database may result in erroneous results for certain JOIN operations.



### Decomposition
- Breaking up tables into more tables
- This can solve update anomalies

#### Normalization
- A technique for producing a set of relations with desirable properties
- A list of tests t o apply on a relational schema in order to determine its quality

#### Functional DEPENDENCIES

- A functional dependency is a constrianty between two sets of attributes in the database
- Universal relation schema R(A1, A2...An)
- A set of attributes X functionally determines a set of attributes Y if the value of X determines a unique value for Y **x -> y**
- FDs are derived from the *meaning* and *interrelationships* of the attributes

## x -> y
- X functionally determines y
- y is functionally dependant on y
- For each value of x, there is exactly one value of y (XZ stands for X U Z)

- **x -> y** Holds if whenever two tuples have the same value for X, they must have the same value for Y

### Inference Rules for FDs
- Given a set of FDs F, we can infer additional FDs that hold whenever the FDs in F hold
- **Closure** of a set F of FDs is the set F_ of all FDs that can be inferred from F
- **F |= X -> y**

- **Reflexive:** if y < x, then x -> y
- **Augmentation:** if X -> y, then XZ -> YZ
- **Transistive:** If x -> y and y -> z then x -> z

IR1, IR2, IR3 (Armstrong’s inference rules) form a sound and complete set of inference rules Slide 

- **Decomposition:** If X → YZ, then X → Y and X → Z
- **Union** If X → Y and X → Z, then X → YZ 
- **Pseudotransitivity** If X → Y and WY → Z, then WX → Z

### A set is minimal if...
- Every dependency in f has a single attribute for its RHS
- We cannot replace any dependency X → A in F with a dependency Y → A, where Y < X and still have a set of dependencies that is equivalent to F
- We cannot remove any dependency from F and have a set of dependencies that is equivalent to F

### Normalization:
The process of decomposing unsatisfactory bad relations by breaking up their atributes. THis is so the resulting designs are of high quality. 

**Denormalization:** The process of storing the join of hgiher normal form relations as a base realtion which is in a lower normal form.

**Normal Form** Condition using keys and FDs of a relation to certify whether a relation schema is in a particular normal form

**First Normal Form:** Expand RHS of relations
![[Pasted image 20261022135202.png]]


**Second Normal Form:** Identify each non-prime attribute, and make sure they depend fully on the Primary Key


![[Pasted image 20261022184359.png]]

![[Pasted image 20261022184609.png]]