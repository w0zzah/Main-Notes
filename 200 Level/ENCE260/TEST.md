### PART A: BASICS

#### Static variables
- Declaring it as static makes it exist on the stack instead of just on the heap.
- Static variables do not need to have malloc or free called on them.


#### Memory
- **The Stack:** The stack variables are declared normally inside a function, these are LIFO (Last in, first out) written variables and the stack frame is destroyed after a function finishes.
- **The Heap:** To create a variable that survives after the function returns you can allocate it to the heap. This is useful for dynamic memory storage where we are creating arrays and objects which size are changing
#### Structs
- **Dot (`.`) vs Arrow (`->`):** The arrow operator is used when working with a pointer and the dot is used with working wit the variable itself
- **Shallow vs. Deep Copy** In C, strings are character arrays assigning stud.name = name creates a shallow copy. This is only copying from the memory address not the text. A deep copy requires allocation memory malloc and copying characters using strcpy


#### Pointers
- **( * ) ~ Keyhole**
- **( & ) @'s somthing)**

```c
int c;
while(isdigit(c = getchar())) {
	result = result * 4 + (c - '0')
}
```
#### Malloc & free
Write a function uint64_t* newCopy(void* array, size_t numElements) Which returns a dynamically-allocated copy of `array`, where `array` is declared in the calling function as: 
uint64_t array[numElements] = {0};
### Answer
```c
uint64_t* newCopy(void* array, size_t numElements)

{

size_t bta = (sizeof(uint64_t) * numElements);

uint64_t* ptr = malloc(bta);

  

if (ptr != NULL) {

memcpy(ptr, array, bta);

}

return ptr;

}
```
#### Valgrind


#### scanf()


## Coding notes:
- 