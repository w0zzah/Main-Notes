#include <stdio.h>
#include <stdint.h>


typedef struct {
    int32_t x;
    int32_t y;
    int32_t z;
} Vector3d;

Vector3d vector(int32_t x, int32_t y, int32_t z)
{
    Vector3d vec = {x, y, z};
    return vec;
}

Vector3d vectorAdd(Vector3d a, Vector3d b)
{
    return vector(a.x + b.x, a.y + b.y, a.z + b.z);
}
int main()
{
    Vector3d v1 = vector(1, 4, -1);
    Vector3d v2 = vector(2, 4, -1);
    Vector3d v3 = vectorAdd(v1, v2);
    printf("(%d, %d, %d)\n", v3.x, v3.y, v3.z);
}