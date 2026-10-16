#include <stdio.h>

size_t readString(char* string, size_t maxStringLength);

int main()
{
    size_t len=0;
    char string[11];
    len = readString(string, 10);
    printf("Read String (%s) of length (%zu)\n", string, len);
}
size_t readString(char* string, size_t maxStringLength)
{
    size_t count = 0;
    int character;

    while (count < maxStringLength && (character = getchar()) != '\n' && character != EOF)
    {
        string[count] = (char)character;
        count++;
    }

    string[count] = '\0';

    return count;
}