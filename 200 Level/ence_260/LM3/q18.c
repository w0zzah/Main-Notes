#include <stdint.h>
#include <stdio.h>

void printArray(int32_t* const nums, size_t n)
{
    int32_t* end = nums + n;
    for (int32_t* p = nums; p < end; p++) {
        int32_t num = *p;
        printf("%d\n", num);
    }
}

int main() {
    int32_t nums[3] = {0, -1, -2};
    printArray(nums, 3);
}