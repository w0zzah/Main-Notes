#include <stdint.h>
#include <stdio.h>

void squareArray(int32_t array[], size_t n)
{
    int size_tt = n;
    for (int i = 0; i < size_tt; i++) {
        array[i] *= array[i];
    }
}

int main() {
    int32_t array[3] = {1, 2, 3};
    squareArray(array, 3);
    printf("%d\n", array[0]);
    printf("%d\n", array[1]);
    printf("%d\n", array[2]);
}