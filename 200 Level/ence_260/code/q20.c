#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <math.h>

void printRoots(float a, float b, float c);

int main (void) {
	printRoots(1, -4, 3);
	printRoots(0, 2, 3);
}


void printRoots(float a, float b, float c)
{
	float disc = ((b * b) - (4 * a * c));

	if (a == 0) {
		printf("Not a quadratic\n");
	}
	else if (disc <= 0) {
		printf("No-real roots");
	} else {
		float root1 = (-b + sqrt(disc)) / (2*a);
		float root2 = (-b - sqrt(disc)) / (2*a);
		printf("Roots are %.4f and %.4f", root1, root2);
	}
}
