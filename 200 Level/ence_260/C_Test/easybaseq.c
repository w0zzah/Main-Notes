#include <ctype.h>
#include <stdint.h>
#include <stdio.h>

uint64_t scanBase4(void)
{
    uint64_t result = 0;
    int c;

    while (isdigit(c = getchar())) {
        result = result * 4 + (c - '0');
    }

    return result;
}

int main ()
{
    uint64_t y = scanBase4();
    printf("%lu\n", y);
}