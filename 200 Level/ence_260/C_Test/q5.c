#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

size_t lineLength(char* string)
{

    size_t index = 0;

    while (string[index] != '\n') {
        index++;
    }
    return index;
}
int main()
{
    printf("%zu\n", lineLength("ABC\nDE"));
}
