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

### Composite Attribute
- When storying a tuple of data we call an attribute that is then linked to another two simple attributes. eexample
```
		/--> First
Name ---
		\--> Last
```

