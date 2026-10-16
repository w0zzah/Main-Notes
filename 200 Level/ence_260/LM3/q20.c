#include <stdio.h>
#include <stdint.h>

int main(void) {
    int32_t numbers[100];
    int32_t input;
    int count = 0;

    do {
        if (scanf("%d", &input) != 1) {
            break;
        }
        
        if (input == -1) {
            break;
        }
        
        numbers[count] = input;
        count++;
        
    } while (count < 100);

    printf("%d numbers entered\n", count);
    
    for (int i = 0; i < count; i++) {
        printf("%d\n", numbers[i]);
    }

    return 0;
}