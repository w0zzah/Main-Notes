

### What is a DBMS?:
- A **DBMS** or **D**ata**B**ase **M**anagement **S**ystem is a collection of software tools and processes used to interact with a database. 
### Data Redundancy:
- Data Redundancy occurs when a database stores the same data in 2 different locations. This can cause the data to take up more space than nessasary and lead to errors as when updating one area of data you must also update the other. Databases aim to reduce this to a minimum through **Normalisation**, where we break down the big tables into smaller linked tables and remove repeat fields. 
### Catalog:
- Data Catalog's hold the information behind the data. This is used to organize and find data containing keyword's, data ownership, definitions etc.
### Data Models: 
- Data Models focus on the structure and link between each piece of data. It's helpful for understanding the link between each piece of data during creation or when altering an old database. There are 3 different types **Conceptual**, **Logical** and **Physical**. 

### Database Phases:
- **Conceptual** provides a data landscape without the requirement of knowledge in the database field. This is extremly useful for when discussing with stakeholders who aren't able to comprehend the other 2.
- **Logical** A detailed map that show's key attributes and relations between each data set. 
- **Physical** Is a system specific model that is able to translate the logical model into database code using languages such as SQL. It defines exact data types storage requirements.


### DBA (Database Administrator):
- The DBA is the team responsible for the entire database enviroment. The start from designing and planning, working through data recovery and system updates, then end of life plan. 
	- **Schema Deinition:** First design and structure of the proposed DB
	- **Security & Auth:** Responsible for data privacy and allowing others to change data 
	- **Maintenance:** Performing backups, Recovering Data, Routine Updates.
	- **Performance:** Making sure the database can efficently run queries.
	- **Storage:**  Define the total physical space a DB can take up

### DB Intension vs Extension:
- The **Intension** of DB refers to the schema, primarily focusing on the definitions of tables, data types, and constraints. This initial structural blueprint acts as a rule-set, that if modified changes the fundamental way we traverse a database.
- The **Externsion** of a DB refers to the actual data stored in the database. 

### Core Data Model Components:
- **Structural:**  Hold's static data types such as tables, entity's their relationships
- **Operational:** Defines action's to interact with the data
- **Integrity:** Enforce's constraints to ensure data consistency through the model

### DDL (Data Definition Language):
- Used to interact with the schema of the database. 

### Database Pro's and Con's
- **Pro's:**
	- **Excellent Data Handling:** Data can be written, removed, and pulled from different people all the same time. 
	- **Structured:** A strong structure lowers the chance for data corruption while allowing ease of searching and manipulation.
- **Con's:**
	- **Complexity:** Running a database is a complex task that require knowledge of SQL or other DBMS languages.
	- **Cost:** To maintain a DB you require money and resources for dedicated servers, Database admins etc.


