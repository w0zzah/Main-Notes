#include <stdio.h>
#include <stdint.h>

int32_t silly(int32_t a, int32_t b, int32_t c)
{
    if (a % 2 != 0) {
        return b;
    } else {
        return c;
    }
}
int main()
{
    printf("%d\n", silly(1, 2, 3));
    printf("%d\n", silly(6, 2, 3));
}