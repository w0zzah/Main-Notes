#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main()
{
    double a;
    double b;
    double c;
    scanf("%lf %lf %lf", &a, &b, &c);
    double result = ((3 * a - -5 * b) / c);
    if (c == 0) {
        printf("Division by zero!\n");
    } else {
        printf("%.4f\n", result);
    }
}

