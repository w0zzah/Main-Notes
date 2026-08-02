#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>


bool isInData(const uint8_t* data, size_t arraySize, const uint8_t* ptr)
{
    return (ptr >= data) && (ptr < (data + arraySize));
}

int main() {
    const uint8_t x = 0;
    const uint8_t thing[3] = {0};
    const uint8_t y = 0;
    printf("%d\n", isInData(thing, 3, &x));
    printf("%d\n", isInData(thing, 3, &thing[0]));
    printf("%d\n", isInData(thing, 3, &thing[1]));
    printf("%d\n", isInData(thing, 3, &thing[2]));
    printf("%d\n", isInData(thing, 3, &thing[3]));
    printf("%d\n", isInData(thing, 3, &y));
}