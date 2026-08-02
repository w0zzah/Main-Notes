#include <stdint.h>
#include <stdio.h>

void printArray(int32_t* array, size_t n)
{   
    int size_tt = n;
    for (int i = 0; i < size_tt; i++) {
        printf("%d\n", array[i]);
    }
}

int main() {
    int32_t list[5] = {0, -1, -2, -3, -4};
    printArray(list, 3);
}