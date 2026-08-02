#include <stdio.h>
#include <stdint.h>

void foo(int32_t* ptr)
{
    printf("Got the value %d\n", *ptr);
    *ptr += 5;
    printf("Changed the value %d\n", *ptr);
}

void bar(const int32_t* ptr)
{
    printf("Got the value %d\n", *ptr);
    ptr += 0;
    printf("Changed the value %d\n", *ptr);
}

int main(void)
{
    int32_t value = 5;

    foo(&value);
    printf("The value is %d\n", value);

    bar(&value);
    printf("The value is %d\n", value);
}