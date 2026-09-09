

DATA MODELLING

At the end of these lectures you should be able to understand the concepts of data modelling importantly you should be able to design database schema according to requirements using the ER and ERR data modals.

## Overview

1. Phases of db design
2. ER
3. Enhanced entity relationship Model
4. Why model
5. Data modelling tools


## Phases of DB Design (check 2-4 fpr diagram)

- Requirement collection
- Conceptual design
- Logical design
- Physical design


## Methodologies for conceptual design
- er (Entity relationship handles basic data structures)
- eer (handles advanced object oriented feature's like inheritance and hierachies)
- design tools
- uml class diagram


## Naming conventions
- **Entities** are specific objects or things in the mini world that are represented in the database
- **Attributes** are properties used to describe an entity
- Each **entity** has a value for each **attribute**
- Each **Attribute** has a **domain**

## Attribute type (slide 2-11)
- Simple(atomic) or composite
	- Gender is simple and composition could be first middle and last name
- Single / multi-valued
	- previous Degrees of a student {previous degrees}
- Stored or derived


## Entity Types and Key Attributes:
- entity type: entities with the same attributes
- If each for every entity they have a unique attribute thsi attribute can be called a key. This is an effective way to identify each unique entity
- A Key must be a composite type and an entity can have multiple keys


## Relationships
- A relationship relates two or more distinct entities with a specific meaning where J works on X
- this can be visually represented with a line connecting through a box.
- The degree of a relationship type is the number of participating entity types

### Type vs Set
- **Type** is the schema description of a relationship and can identify the the name and participating entity types, can also identify certain relationship constraints
- **Set** is the current set of relationship instances represented in the database and hold the state of type

## Weak entity Type
An entity type that does not have a key attribute is a weak entity type and must participate in an identified relationship with an owner or identifying entity type. They are identified by the combination of the partial key of the weak entity type and the particular entity they are related to in the identify entity 

## Integrity of component of ER
- Key attribute
- Cardinality Ratio
- Participation Constraint


## Structural Constraints
- We have a minimum and maximum
- Specifies that each entity e in E participates at least min and at most max in r

