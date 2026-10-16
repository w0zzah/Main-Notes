#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

void printPrimesInRange(uint32_t n1, uint32_t n2)
{
    // uint32_t range = n2 - n1;
    for (int i = n1; i <= n2; i++) {
        bool isPrime = true;
        for (int y = i; y < i; y++) {
            if (i % y == 0) {
                isPrime = false;
             }
        }
      
        if (isPrime) {
            printf("%d\n", i);
        }
    }
}

int main ()
{
    int32_t num = 31;
    int32_t* ptr = NULL;
    ptr = &num;
    *ptr = 62;
    printf("%d, %d\n", *ptr, num);
}


