#include <stdint.h>
#include <stdio.h>

void printDigitName(uint8_t digit);
int32_t gringe(int32_t boink, int32_t flunk);

void main(void)
{
	printf("%d\n", gringe(23, 24));
	printf("%d\n", gringe(23, 23));
	printDigitName(2);
	printDigitName(-1);
	printDigitName(4);
	printDigitName(7);
	char c;
	int count;
	
}

int32_t gringe(int32_t boink, int32_t flunk)
{
    return (boink == flunk) ? 42 : (flunk - 11);
}

void printSquares(uint32_t n)
{
    int i;
    for (i = 1; i <= n; i++) {
        int res = i * i;
        printf("%d\n", res);
    }
}

void printDigitName(uint8_t digit)
{
	switch(digit) {
		case 1:
			printf("One\n");
			break;
		case 2:
			printf("Two\n");
			break;
		case 3:
			printf("Three\n");
			break;
		case 4:
			printf("Four\n");
			break;
		case 5:
			printf("Five\n");
		default:
			printf("Out of bounds\n");
	}
}


void meetsCondition(int64_t x)
{
    if ((((x % 2) == 0) && (x > 0)) || (((x % 2) != 0) && (x < 0))) {
        puts("true");
    } else {
        puts("false");
    }
}
