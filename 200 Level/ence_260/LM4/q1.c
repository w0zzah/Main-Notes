#include <stdint.h>
#include <stdio.h>


struct PolarVec_s {
	int32_t radius;
	float  angle;
};

int main(void) {
	struct PolarVec_s v;
	v.radius = 1;
	v.angle = 180;
	printf("%d\n", v.radius);
	printf("%.1f\n", v.angle);
}
