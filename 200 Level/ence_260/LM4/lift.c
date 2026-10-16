#include <stdint.h>
#include "lift.h"

Lift lift_init(uint8_t maxPassengers, int16_t startFloor)
{
    Lift lift = {
        .floor = startFloor,
        .currentPassengers = 0,
        .maxPassengers = maxPassengers
    };

    return lift;
}

void lift_onboard(Lift* lift, uint8_t peopleOff, uint8_t peopleOn)
{
    lift->currentPassengers += (peopleOn - peopleOff);
}

int16_t lift_goToFloor(Lift* lift, int16_t floor)
{
    if (lift->currentPassengers > lift->maxPassengers) {
        return lift->floor;
    } else {
        lift->floor = floor;
    }
    return lift->floor;
}