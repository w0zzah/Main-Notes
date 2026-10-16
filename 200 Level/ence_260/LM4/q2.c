#include <stdint.h>
#include <stdio.h>

struct PolarVec_s {
	uint32_t radius;
	float angle;
};

struct PolarVec_s initPolarVec(uint32_t radius, float angle){
	struct PolarVec_s v;
	v.radius = radius;
	v.angle = angle;
	return v;
}

void printPolarVec(struct PolarVec_s v)
{
	printf("%u : %.1f\n", v.radius, v.angle);
}

int main(void) {
	struct PolarVec_s v = initPolarVec(5, 3.14);
	printPolarVec(v);
	v.angle = 6.28;
	printPolarVec(v);
}



