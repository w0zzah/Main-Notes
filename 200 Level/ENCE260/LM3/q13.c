#include <stdint.h>
#include <stdio.h>

int32_t accumulator(int32_t value);

int main(void)
{
    accumulator(3);
    accumulator(2);
    printf("%d\n", accumulator(5));
}

int32_t accumulator(int32_t value)
{
    // Can use static here as it gets put in data segment instead of stack
    static int32_t accumulatorSum = 0;
    accumulatorSum += value;
    return accumulatorSum;
}