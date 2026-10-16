#include <stdio.h>

int main(void)
{
    int character;
    while ((character = getchar()) != -1) {
        printf("%d\n", character);
    }

    return 0;
}