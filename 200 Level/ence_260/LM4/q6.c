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

void printCoord(Coord coord) {
	printf("(%.2f, %.2f, %.2f)\n", coord.lat, coord.lon, coord.alt);
}

void printCoordPtr(const Coord* coord) {
	printf("(%.2f, %.2f, %.2f)\n", (*coord).lat, (*coord).lon, (*coord).alt);
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
Coord everest = {
    .lat = 27.988056,
    .lon = 86.925278,
    .alt = 8848.86
};
printCoordPtr(&everest);
}



