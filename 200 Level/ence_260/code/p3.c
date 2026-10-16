#include <stdio.h>
#include <stdint.h>

uint32_t countRushes(float screeHeight, float rushHeight, float slideBack);


int main (void) {
	printf("%d\n", countRushes(100, 50, 10));
	printf("%d\n", countRushes(100, 100, 90));
	printf("%d\n", countRushes(0, 100, 30));
}

uint32_t countRushes(float screeHeight, float rushHeight, float slideBack) {
	uint32_t rushes = 0;

	while (screeHeight > 0) {
		rushes++;
		screeHeight -= rushHeight;

		if (screeHeight <= 0) {
			break;
		} else {
			screeHeight += slideBack;
		}
	}

	return rushes;
}

