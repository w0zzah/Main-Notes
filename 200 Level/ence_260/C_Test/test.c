#include <ctype.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

size_t lineLength(char* string)
{
    int counter = 0;
    for (int i = 0; i < sizeof(string); i++) {
        if (string[i] == '\n') {
            counter = i;
        }
    }
    return counter;

}




int main()
{
    uint16_t y = scanBase2();
    printf("%u\n", y);
}