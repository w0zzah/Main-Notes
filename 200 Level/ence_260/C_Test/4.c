#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>



void findInArray(int64_t* array, size_t n, int64_t value, int64_t** foundValueDest)
{
    *foundValueDest = NULL;
    for (int i = 0; i < n; i++) {
        if (array[i] == value) {
            *foundValueDest = &array[i];
            break;
        }
    }
}

int main()
{
    int64_t array[6] = {0, 2, 4, 6, 8, 10};
    int64_t* foundValue = NULL;
    findInArray(array, 6, 8, &foundValue);
    if (foundValue != NULL) {
        printf("%ld == %ld\n", *foundValue, array[4]);
    }
}