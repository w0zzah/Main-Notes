#include <stdio.h>
#include <ctype.h>


int main(void)
{
    int character;
    while ((character = getchar()) != EOF) {
        if (character == 10) {
            printf("'\\n'\n");
        } else if (isdigit(character)) {
            printf("'%c': Digit %d \n", character, character - '0');
        } else if (isalpha(character)) {
            if (isupper(character)) {
            printf("'%c': Letter %d \n", character, character - 'A' + 1);
            } else {
                printf("'%c': Letter %d \n", character, character - 'a' + 1);
            }
        } else {
            printf("'%c': Non-alphanumeric\n", character);
        }
    }
}