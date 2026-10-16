#ifndef LIFT_H
#define LIFT_H
#include <stdint.h>


typedef struct {
	int16_t floor;
    uint8_t currentPassengers;
	uint8_t maxPassengers;
} Lift;

Lift lift_init(uint8_t maxPassengers, int16_t startFloor);

void lift_onboard(Lift* lift, uint8_t peopleOff, uint8_t peopleOn);

int16_t lift_goToFloor(Lift* lift, int16_t floor);

#endif