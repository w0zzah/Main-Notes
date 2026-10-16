#include "temp.h"
#include <stdint.h>
#include <stdio.h>

static float convert(float temp, Unit funit, Unit tunit)
{

    float celsius = temp;
    switch (funit) {
        case FAHRENHEIT:
            celsius = (temp - 32.0) * (5.0f / 9.0); 
            break;
        case KELVIN: 
            celsius = temp - 273.15; 
            break;
        default:
            break;
    }

    switch (tunit) {
        case FAHRENHEIT:
            return (celsius * (9.0 / 5.0)) + 32.0;
        case KELVIN:
            return (celsius + 273.15);
        default: 
            return celsius;
    }
}

void temp_set(Temp* temp, float value, Unit unit)
{
    temp->temperature = value;
    temp->unit = unit;
}

void temp_print(const Temp* temp, Unit unit)
{
    float display_temp = convert(temp->temperature, temp->unit, unit);
    switch (unit) {
        case FAHRENHEIT:
            printf("%.2f deg F\n", display_temp);
            break;
        case KELVIN:
            printf("%.2f K\n", display_temp);
            break;
        default: 
            printf("%.2f deg C\n", display_temp);
    }
}