// ANY MODIFICATIONS MADE HERE WILL BE IGNORED
#include <stdint.h>
#include <stdio.h>

#include "rect.h"

int main(void)
{
    uint32_t width;
    uint32_t height;
    scanf("%d %d", &width, &height);
    
    Rect rect;
    rect_set(&rect, width, height);
    printf("Area = %d\n", rect_area(&rect));
    printf("Perimeter = %d\n", rect_perimeter(&rect));
}