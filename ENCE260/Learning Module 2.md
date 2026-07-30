### Expressions:
- An expression evaluates to a variable
	- e.g(1, x+ 1, 3*y, 2)

### Statements:
- A Statement is a simple assignation of a variable
	- e.g (x = 10, y = x+ 1, x += (2 + 3*y))

### Declarations:
- A Declaration is when we assign a type to an expression or statement
	- e.g (int32_t x = 0, int32_t y)

### Functions:
- Should be called at the start of a program to init and then written after main.

```c
uint32_t square(in32_t x);
void printNumber(int32_t x);

int main(void)
{
	printNumber(7)
	printf("%d\n", square(-5))
}

void printNumber(int32_t x)
{
	printf("%d\n)", x);
	x ++ <-- Note: This increase in x is only present in THIS func
}

unint32_t square(int32_t x)
{
	return x * x;
}
```


