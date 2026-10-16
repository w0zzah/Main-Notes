#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>





bool checkOverlap(const int32_t arr1[], size_t len1, const int32_t arr2[], size_t len2)
{
    return &arr1[len1] > &arr2[0];
}


int main()
{
    int32_t data[2048] = { 1, 2, 3, 4, 5, 6, 7, 8 };
    int32_t* a = data + 0;
    int32_t* b = data + 4;
    printf("%s\n", checkOverlap(a, 8, b, 10) ? "True" : "False");
}