#### Intro
- Recall that you can create multi-dimensional arrays, such as this datalog with 15 rows and 5 columns with **unint16_t datalog\[15]\[5];**
- Note that datalog is effectively just a single pointer to type unit16_t which is being used to point to a singular array with 15\*5 elements. The compiler helps with keeping track of the appropriate index into the singular array things with correct use of the two indices. Datalog should not be confused with the double pointer discussion below. 
```c
#include <stdio.h>
#include <stdint.h>

void printData(int8_t** data, size_t numberLines)
{
    for (size_t i=0; i < numberLines; i++) {
        printf("Line %zu, first element is %d\n", i, data[i][0]);
    }
}

int main()
{
    int8_t dataline1[] = {1, 2, 3, 4, 5};
    int8_t dataline2[] = {6, 7, 8, 9, 10, 11, 12};
    int8_t* datalines[] = {dataline1, dataline2};

    printData(datalines, 2);
} 
```


#### Parsing in parameters for main:
- int is used as an error code back to the operating system
- argc is the integer count of the number of strings in the array argv
- argv is an array of string literals 
```c
#include <stdio.h>

int main(int argc, char* argv[])
{
    for (int i = 0; i < argc; i++) {
        printf("[%d] %s\n", i, argv[i]);
    }

    return 0;
}
```

#### Function Pointers:
- code is also stored in the memorym this means we can use pointers with it as well. In C this is accomplished via function pointers. Function pointers are pointers that contain the address of the start of a functions compiled code in memory. They let us store the identity of one function out of all those in the program.

**E.G:** 
If we have a function :  *int32_t funct(int32_t arg1, uint8_t arg2);*
the we declare it like  - > *int32_t (\*pfunc)(int32_t, uint8_t); = &func*
*note: If we want to call it we dereference it first with int32_t retVal = (\*pfunc)(a, b);*



