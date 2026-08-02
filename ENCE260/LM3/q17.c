#include <stdint.h>
#include <stdio.h>

void printArray(int32_t* nums, size_t n) {
    for (int i = 0; i < n; i++) {
        printf("%d\n", *nums++);
    }
}

int main() {
    int32_t nums[3] = {1, 2, 3};
    printArray(nums, 3);
}