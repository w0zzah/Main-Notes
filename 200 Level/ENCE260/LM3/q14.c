#include <stdio.h>
#include <stdint.h>

void foo(int32_t val)
{
    printf("Got the value %d\n", val);
    val += 5;
    printf("Changed the value %d\n", val);
}

void bar(const int32_t val)
{
    printf("Got the value %d\n", val);
    // val += 5;
    printf("Changed the value %d\n", val);
}

int main(void)
{
    int32_t value = 5;

    foo(value);
    printf("The value is %d\n", value);

    bar(value);
    printf("The value is %d\n", value);
}