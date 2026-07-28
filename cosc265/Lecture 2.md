Database features

Data catalog (dictionary) 


Description of the database (meta=-data)

Allows DBMS to work with different DBs

Data abstraction
DAta integrity
Data Independence
- Logical & Physical data independence

Physical Data independence means you can changed the internal schema but nothing changes the actual info

Logical inbdependance is you change the conceptual schema but nothing changes at the end users perception e.g adding new entries of data

People involved with DBs -> Actors is db admins, designers and end users:
Admins can create, manage, main structures, backup, tune for performance.
EU -> Casual / parametric ("canned or same action again n again) / Sophisticated / Stand alone (full use)
DBMS designers / Tool developers

## Data Model (set of concepts used to describe structure)

We need a tool that can model the real world in a way that the achieved representation is abstract enough to suppress unnecessary details. 

### Schemas vs Instance
DB schema is the desc of a db 
schema displays some aspects of a db changes often
db instance is data stored
db state is the extension or occurence

DB stateL refers to content of db at amoment in time

initial database state is a snapshot

## Components of data models

structural, Integrity, Oeprational

## Categories 




# DBMS


## DBMS Language
- Data Definition Language
- View defininition
- Storage Definition
- Data manipulation



## INterfaces
- Stand alone query language interfaces
- programmer interfaces
- User friendly interfacesa


## Other types
- Speech as inout out
- web browser
- parametric / bank tellers using keys
- e.g create acc, set system paramas, change chema or accesssoath


## DB System Util
- To perform funcs such as
- - Loading data
- Backing up data 
- Reorganizing db
- Report generation
- Performance Monitor

## Other Tools
- Data dictionary / repo 
- sotre chema active data & passive data





## Whenever the user interacts with a DB..
- They interact with the System Catalog or Data Dictionary.  (Check out slides 1-41 for a diagram)


## Architectures: 
We primarily will look at a centralised DBMS, although other acrhitectures such as client server architecture, specialised servers, clients and DBMS servers


## Clients
- Provide appropriate interfaces and a client version of the sustem to access and utlilize the server resources clients may ebe diskless machines or pcs

## DBMS Approach
- Potentional for dbms is good for enforcing standards reduce application dev time, flexible, available for up to daate info and economies of scale

- Negatives: Complexity, size, cost, additional hardware cost, Performance, higher impact of failure

## When not to use a DBMS
- Small data set, well defined not going to change, real time reqs, access by multiple users not req