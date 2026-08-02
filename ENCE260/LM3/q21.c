#include <stdint.h>
#include <stdio.h>

void printSquaredArray(const int32_t array[], size_t n)
{
    int size_tt = n;
    for (int i = 0; i < size_tt; i++) {
        printf("%d\n", array[i] * array[i]);
    }
}

int main() {
    const int32_t array[3] = {-1, -2, -3};
    printSquaredArray(array, 3);
}