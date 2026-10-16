#include <stdint.h>
#include <stdio.h>

int32_t index2d(int32_t* array, size_t width, size_t i, size_t j)
{
    // just a 1d array -> 1 * 3 + 1 - 4 or [1][1] ->
    return array[i * width + j];
}

int main() {

    int32_t array[3][3] = {{314, 15, 9}, 
                       {2, 65, 35},
                       {8979, 323, 84}};
    printf("%d\n", index2d((int32_t*)array, 3, 1, 1));
}