#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdlib.h>
#include <string.h>

uint64_t* newCopy(void* array, size_t numElements)
{
    size_t bta = (sizeof(uint64_t) * numElements);
    uint64_t* ptr = malloc(bta);
    if (ptr != NULL) {
        // Copy the data from the source array into the new allocation
        memcpy(ptr, array, bta);
    }
    return ptr;
}


int main()
{
    uint64_t array[3] = {1, 2, 3};
    uint64_t* copy = newCopy(array, 3);
    array[1] = 4;
    for (size_t i = 0; i < 3; i++) {
        printf("%lu\n", copy[i]);
    }
    free(copy);
}