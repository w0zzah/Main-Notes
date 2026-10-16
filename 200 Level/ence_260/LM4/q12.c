

#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef enum {
    REVERSE = -1,
    NEUTRAL = 0,
    FIRST = 1, 
    SECOND = 2, 
    THIRD = 3, 
    FOURTH = 4,
    FIFTH = 5,
} Gear;

int main(void) {
Gear currentGear = FIRST;
printf("%d\n", currentGear + THIRD);
}