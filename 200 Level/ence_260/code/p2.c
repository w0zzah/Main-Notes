#include <stdio.h>
#include <stdlib.h>
#include <stdint.h> // Required for uint32_t

// 1. Added the missing semicolon at the end of the function prototype
uint32_t countRushes(float screeHeight, float rushHeight, float slideBack);

int main(void) {
    printf("%d\n", countRushes(100, 50, 10));
    printf("%d\n", countRushes(100, 100, 90));
    printf("%d\n", countRushes(0, 100, 30));
    
    return 0;
}

uint32_t countRushes(float screeHeight, float rushHeight, float slideBack) {
    // 2. Created a variable to track the number of rushes
    uint32_t rushes = 0; 
    
    // 3. Changed to a standard while loop to safely handle starting heights of 0
    while (screeHeight > 0) {
        rushes++;
        screeHeight -= rushHeight;
        
        // 4. Fixed typo: changed "screeheight" to "screeHeight"
        if (screeHeight <= 0) {
            break;
        } else {
            screeHeight += slideBack;
        }
    } 
    
    // 5. Added the missing return statement
    return rushes; 
}