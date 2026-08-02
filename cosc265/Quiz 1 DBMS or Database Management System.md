

### What is a DBMS?
- A **DBMS** or **D**ata**B**ase **M**anagement **S**ystem is a set of software programs used to create, maintain and operate a database. 
### Data Redundancy
- Occurs when a database contains the same data item more than once. This wastes space and causes update errors. Databases aim to control redundancy (via normalisation) rather than eliminate it entirely, as some controlled redundancy can improve performance. 
### Data Catalog (metadata)
- Data Catalog's hold the information behind the data. This is used to organize and find data containing keyword's, data ownership, definitions etc.
### Data Models
- A set of concepts that describe data structure and relationship's present in the database. A blueprint used during creation and modification.


### Database Phases
**Conceptual** *Independant* 
- Provides a data landscape without the requirement of knowledge in the database field. This is extremly useful for when discussing with stakeholders who aren't able to comprehend the other 2.
**Logical** *Dependant* 
- A detailed map that show's key attributes and relations tailored to specific data models. 
**Physical** *Dependant* 
- A system specific model that is able to translate the logical model into database code using languages such as SQL. It defines exact data types storage requirements.



### DBA (Database Administrator)

The DBA is the team responsible for the entire database enviroment. The start from designing and planning, working through data recovery and system updates, then end of life plan. 

- **Schema Deinition:** First design and structure of the proposed DB
- **Security & Auth:** Responsible for data privacy and allowing others to change data 
- **Maintenance:** Performing backups, Recovering Data, Routine Updates.
- **Performance:** Making sure the database can efficently run queries.
- **Storage:**  Define the total physical space a DB can take up


### DB Intension vs Extension

- **Intension** of DB refers to the schema, primarily focusing on the definitions of tables, data types, and constraints. This initial structural blueprint acts as a rule-set, that if modified changes the fundamental way we traverse a database.
- **Externsion** refers to state of the data in the database. It changes often as data is modified.


### Core Data Model Components
- **Structural:**  Hold's static data types such as tables, entity's their relationships
- **Operational:** Defines action's to interact with the data
- **Integrity:** Enforce's constraints to ensure data consistency through the model

### Database Languages (DDL, DML, DCL, TCL, VDL)
- **DDL:** Interact with **D**atabase Schema
- **DML:** **M**anipulate Data
- **DCL:** **C**ontrol permission's
- **TCL:** **T**ransaction's between data manipulation
- **VDL:** Change a user's **V**iew of data to be modified

### Database Pro's and Con's
- **Pro's:**
	- **Excellent Data Handling:** Data can be written, removed, and pulled from different people all the same time. 
	- **Structured:** A strong structure lowers the chance for data corruption while allowing ease of searching and manipulation.
- **Con's:**
	- **Complexity:** Running a database is a complex task that require knowledge of SQL or other DBMS languages.
	- **Cost:** To maintain a DB you require money and resources for dedicated servers, Database admins etc.


