#include <stdio.h>
#include <stdint.h>


uint64_t scanBase2(void)
{
    int c;
    uint64_t t = 0;
    do {
        c = getchar();
    } while (c != 'a');
    printf("%c", c);
    return t;
}

int main() {
    scanBase2();
}