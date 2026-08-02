#include <stdint.h>
#include <stdio.h>

void convertDistance(const double* metres, double* centimetres, double* kilometres) {
    *centimetres = *metres * 100;
    *kilometres = *metres / 1000;
}

int main() {
    const double metres = 100;
    double centimetres = 0;
    double kilometres = 0;
    convertDistance(&metres, &centimetres, &kilometres);
    printf("%.1e m, %.1e cm, %.1e km\n", metres, centimetres, kilometres);
}