#ifndef RECT_H
#define RECT_H
#include <stdint.h>
#include <stdio.h>

typedef struct {
    uint32_t width;
    uint32_t height;
} Rect;

void rect_set(Rect* rect, uint32_t width, uint32_t height);
uint32_t rect_area(const Rect* rect);
uint32_t rect_perimeter(const Rect* rect);
#endif
