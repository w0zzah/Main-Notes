#ifndef BULB_H
#define BULB_H

#include <stdint.h>


typedef enum {
    CELSIUS,
    FAHRENHEIT,
    KELVIN
} Unit;

typedef struct {
    float temperature;
    Unit unit;
} Temp;


void temp_set(Temp* temp, float value, Unit unit);
void temp_print(const Temp* temp, Unit unit);

#endif
