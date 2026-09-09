#include <stdio.h>
#include <stdint.h>


void printViaPtr(int16_t*);
void print2Ints(int16_t number1, int16_t number2);
void swap(uint8_t* address1, uint8_t* address2);

int main() 
{
    uint8_t i = 10, j = 20;
    swap(&i, &j);
    printf("%d %d\n", i, j);
}

void swap(uint8_t* address1, uint8_t* address2)
{
    // temp value = address1 value
    uint8_t temp = *address1;
    // address1 value = adress2 value
    *address1 = *address2;
    // address2 value = temp value
    *address2 = temp;
}