#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define FREEZING_PT 6000
#define SCALE_FACTOR (5 / 9)


int main(void)
{
	int32_t fahrenheit = 50;
	int32_t celsius = 0;

	celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;

	printf("%d degrees Fahrenheit is equivalent to %d degrees Celsius\n", fahrenheit, celsius);

	return EXIT_SUCCESS;
}
