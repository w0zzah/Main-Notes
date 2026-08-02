#include <stdio.h>
void oof(char* p1, char* p2)
{
    *p1 = *p2;
}

int main(void)
{
    char c = 0;
    char other = '#';
    scanf("%c", &c); // Reads a single character into c
    oof(&other, &c);
    printf("%c\n", other);
}