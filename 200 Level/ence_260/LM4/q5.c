#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
	float lat;
	float lon;
	float alt;
} Coord;

bool isBelowSeaLevel(Coord coord)
{
	return (coord.alt < 0);
}

uint64_t numBelowSeaLevel(const Coord coords[], size_t n) {
	int count = 0;
	for (size_t i = 0; i < n; i++) {
		if (isBelowSeaLevel(coords[i])) {
			count++;
		}
	}
	return count;
}

int main(void) {
Coord coords[5];
for (size_t i = 0; i < 5; i++) {
    coords[i].lat = ((float)i - 2)*15;
    coords[i].lon = ((float)i - 2)*-15;
    coords[i].alt = ((float)i - 2)*100;
}
printf("%lu\n", numBelowSeaLevel(coords, 5));
}



