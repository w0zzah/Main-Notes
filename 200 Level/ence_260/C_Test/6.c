#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdlib.h>
#include <string.h>


int16_t func(int16_t x)
{
    return x/2; //Only an example - could be anything. 
}


int16_t callPassedFunc(int16_t (*funcPtr)(int16_t), int16_t arg)
{
    return funcPtr(arg);
}

int main()
{
    int16_t arg = 10;
    int16_t directRetVal = func(arg);
    int16_t indirectRetVal = callPassedFunc(&func, arg);
    printf("%d\n", directRetVal == indirectRetVal);
    return 0;
}