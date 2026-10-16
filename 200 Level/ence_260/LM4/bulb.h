#ifndef BULB_H
#define BULB_H

#include <stdint.h>
typedef struct {
    uint32_t serialNumber;
    int32_t model;
} Bulb;


Bulb bulb_sellModel(uint8_t model);
void bulb_display(Bulb bulb);
uint32_t bulb_numSold(uint8_t model);


#endif
