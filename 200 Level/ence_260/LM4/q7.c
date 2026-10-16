#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
	int32_t x;
	int32_t y;
	int32_t vx;
    int32_t vy;
} Particle;

void setVelocity(Particle* particle, int32_t vx, int32_t vy)
{
    particle->vx = vx;
    particle->vy = vy;

}
void updatePosition(Particle* particle)
{
    particle->x += particle ->vx;
    particle->y += particle ->vy;
}
int main(void) {
Particle mote = {
    .x = 0,
    .y = 1,
    .vx = 0,
    .vy = 0
};
setVelocity(&mote, 3, 4);
updatePosition(&mote);
printf("v = %d, %d\n", mote.vx, mote.vy);
printf("x = %d, y = %d\n", mote.x, mote.y);
}



