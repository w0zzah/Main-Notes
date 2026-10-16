#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int32_t x;
    int32_t y;
} Vec;

typedef struct {
    Vec position;
    Vec velocity;
} Particle;

Vec vecSum(Vec v1, Vec v2) 
{
    Vec out;
    out.x = v1.x += v2.x;
    out.y = v1.y += v2.y;
    return out;
}
void setVelocity(Particle* particle, int32_t vx, int32_t vy)
{
    particle->velocity.x = vx;
    particle->velocity.y = vy;

}
void updatePosition(Particle* particle)
{
    particle->position = vecSum(particle->position, particle->velocity);
}

int main(void) {
Particle mote = {{0, 1}, {0, 0}};
setVelocity(&mote, 3, 4);
updatePosition(&mote);
printf("v = %d, %d\n", mote.velocity.x, mote.velocity.y);
printf("x = %d, y = %d\n", mote.position.x, mote.position.y);
}