

#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef enum {
    NORTH, 
    EAST, 
    SOUTH, 
    WEST
} Heading;

int main(void) {
Heading dir = NORTH;
printf("%d\n", dir == NORTH);
}