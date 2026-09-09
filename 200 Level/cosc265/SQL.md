

### history:
Originally started as SEQUAL a language developed for system R in 1970


SQL is a combination of DDL VDL and DML all in one.

 - **DDL**: Manipulate database objects (tables, constraints, domains, procedures, ...)
- **VDL** (views)
- **DML**: Manipulate data (select, insert, update, and delete data)
- Transaction control
- Integrity control (DDL) 
- Embedded and dynamic SQL
- Authorization 


### Oracle in SQL:
- In oracle SQL statements may be..
- entered directly from SQL*Plus
- entered through GUI interface (SQL DEveloper)
- embeed within programs
- used in app dev tools


### Elements of SQL Statements
- **SQL VS ER** A table can have two or more typles that are identical in all their attr vals
- a SQL table is a multi set
- SQL can be constr to be sets specify PK or UNIQUE attr or using DISTINCT


### Naming conv
- DBNAME up to 8 chars
- no more than 30 alph chars 
- must not include sys_
- case insensitive


### Data types
- Even when two DBMS have the same data type they can be dufferent due to the numeric valyues such as integer in etc
Also can vary based off of Character types



### Data types CONT
Abstract types like date time mone
- default dd mmm YY
- bianry
- Bool
- TIME
- TIMESTAMP
- INTERVAL


### Operators
- Artihmitic
- String concentation
- Comparasions
- Logical
- Set


### Functions:
- Scalar funcs
- type conversions
- Numeric
- String
- Date time functioms
**Can also do aggregate funcs**


### etc
**Expression is an attr**
Data definition in SQL


### Steps for creating tables 
1. What are the attrs to be stroed
2. What are the data types for the attr
3. Which colyumns make the primary key
4. Are there any foregin keys?
5. Which Columns do not allow NULLS
6. Which columns do not allow duplicates
7. Are there default values for certain columns
8. Are there any limitation on the values allowed in attributes?




