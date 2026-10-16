#include <stdio.h>
#include <stdint.h>

int16_t addOdd(const int16_t data[], size_t n)
{
    int16_t result = 0;
    for (int i = 1; i < n; i += 2) {
        result += data[i];
    }
    return result;
}
int main()
{
    int16_t data[10] = {1, 2, 3, 4, 7, 8, 9, 9, 2, 1};
    printf("%d\n", addOdd(data, 10));
}