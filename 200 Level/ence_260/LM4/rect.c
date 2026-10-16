#include <stdint.h>
#include "rect.h"

void rect_set(Rect* rect, uint32_t width, uint32_t height)
{
    rect->width = width;
    rect->height = height;
}

uint32_t rect_area(const Rect* rect)
{
    return rect->width * rect->height;
}

uint32_t rect_perimeter(const Rect* rect)
{
    return (rect->width * 2) + (rect->height * 2);
}