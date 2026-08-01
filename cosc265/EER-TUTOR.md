For each **course** a **student** has taken we need to know the final **grade**. Each **course** has a unique course **code** and a student has his/her student **id**

- **Student** is an entity with the attribute **id**
- **Course** is an entity with the attribute **code** 
- **Takes** is the relationship between the two. This is instantiated by **Grade**

#### Q3: "The values of the completeness constraint are:"
- Disjoint or partial
- Dosjoint or overlapping
- **Partial or total**
- Overlapping or partial

#### **Q4: ** If an entity types has a multi valued attribute then...
1. Each entity of this type can have one of several values for that attribute
2. **There are some entities of this type that have more that one value for that attribute**
3. Each entity of this type has more than one value for that attribute
4. There are many valid values for that attribute

#### **Q5:** A weak entity type participates in the identifying relationship type...
1. **Always totally**
2. Always partially
3. Either totally or partially


#### Students[ER]
- Students is an entity with multiple attributes. Their key attribute is something that is unique to them.
- Student's have the attribute name, that has two branching attributes first and last.


# Entity Types:


- #### Regular Entity (Strong Entity):
	- An entity that exists independently of any other entity in the database. It has its own unique identity and is uniquely identified by its own **Primary Key**.
	
- #### Regular Entity (Weak Entity):
	- An entity that is dependant on an owner entity, using a partial key to discriminate the difference between it and the other children. 

### When to use partial Keys ~
- An employee is a Strong entity as it carries his own primary key that can be used to distinquish them from other employees. This would be his **Primary Key**. Then if their car was on the database, where the car's key would be its number plate, then the partial key for their car would be **Primary Key** + **Plate No.** = **Partial Key**