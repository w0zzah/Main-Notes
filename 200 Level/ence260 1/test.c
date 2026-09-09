#include <stdio.h>
#include <stdint.h>


int main(void)
{
	int32_t number = 10;
	int32_t result = 0;
	result = 5 * ++number;
	printf("%d\n", result);
}
