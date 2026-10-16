//MODIFYING HAS NO EFFECT
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include "temp.h"



int main(void)
{
    Temp temp;
    float value;
    scanf("%f", &value);
    temp_set(&temp, value, CELSIUS);
    temp_print(&temp, CELSIUS);
    temp_print(&temp, FAHRENHEIT);
    temp_print(&temp, KELVIN);
}