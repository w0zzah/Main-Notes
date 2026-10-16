#include <ctype.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>

uint64_t scanBase4(void)
{
    uint64_t array[10];
    int i = 0;
    char c;
    while (isdigit((c = getchar()))) {
        array[i] = c;
        i++;
    }
    int power = i - 1;
    uint64_t result = 0;
    int value;
    for (int j = 0; j < i; j++) {
        value = array[j] - '0';
        result += (value * pow(4, power));
        power--;
    }
    return result;
}