## Structuring Data and Code
### Goals
Python and Java provide classes and modules/packages to help you structure larger programs. C has neither of these but has similar cunstrcuts that make it still possible to build large systems. This lab introduces C data structures which allow you to organise your data into an amalgam of related items. C typedefs are also introduced in part a convenient way to not have to type struct all the time, but mostly for typechecking. The lab shows how larger programs can be broken down into a nmber of files, each containing a set of related functions and their data.

### Data Types:
A var in c has two aspects, their data and their type. The type tells the machine how to interpret the data. Built in types such as float, double and int have a different pattern of raw bits than float even if they have the same value. The compiler will do the conversion between numerical types for us and attempt to preserve their values. 

## Initialising Structs
```c
struct vector_s {
	uint32_t x;
	uint32_t y;
	uint32_t z;
}

struct vector_s initVector(uint32_t x, uint32_t y, uint32_t z)
{
	struct vector_s v;
	.x = x;
	.y = y;
	.z = z;
	return v;
}

void printVector_s(struct vector_s v)
{
	printf("", v.x, v.y, v.z)
}
```


## User Defined Types - typedef
typedef unit8_t Byte;


```c
typedef struct Vector_s Vector;
struct Vector_s {
	int32_t x;
	int32_t y;
}
```

```c
typedef struct {
	int32_t x;
	int32_t y;
} Vector;
```

typedef struct {
	
}

### Forward Declarations
In c, a func must be declared before its used. This can be similarly applied to header files or (.h). These are c/C++ files that store code declarations, function prototypes, macros and class definitions to share accross multiple files. When writting a header file we need to encircle it in #ifndef & #endif

```c
#ifndef MONTHS_H
#define MONTHS_H
typedef enum {
	JAN,
	ETC,
} Month;
#endif
```
these files should only contain the stuff other mudles need to know about 
