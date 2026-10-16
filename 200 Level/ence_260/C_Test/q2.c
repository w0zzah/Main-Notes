#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// A custom function to read characters into a buffer and convert to a double
double read_double() {
    char buffer[64];
    int i = 0;
    int ch;

    // 1. Skip any leading whitespace (spaces, newlines, tabs)
    do {
        ch = getchar();
    } while (isspace(ch));

    // 2. Read characters (digits, minus signs, decimals) until a space or EOF
    while (ch != EOF && !isspace(ch)) {
        if (i < 63) { // Leave room for the null terminator
            buffer[i++] = (char)ch;
        }
        ch = getchar();
    }
    
    // 3. Null-terminate the string so atof() can read it properly
    buffer[i] = '\0'; 

    // 4. Convert the string buffer into a double precision float
    return atof(buffer);
}

int main() {
    double a, b, c;

    // Call our custom function three times to populate the variables
    a = read_double();
    b = read_double();
    c = read_double();

    // Handle the zero check mandated by the prompt
    if (c == 0.0) {
        printf("Division by zero!\n");
    } else {
        // Calculate the result and print to exactly 4 decimal places
        double result = (-1.0 * a * -1.0 * b) / c;
        printf("%.4lf\n", result);
    }

    return 0;
}