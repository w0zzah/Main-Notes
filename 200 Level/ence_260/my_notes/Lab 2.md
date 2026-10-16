```c
#include <avr/io.h>
#include "system.h"
#include "led.h"
#define DELAY_TICKS 3906  

int main (void)
{
	system_init ();
	led_init ();
	TCCR1A = 0x00;
	TCCR1B = 0x05;
	TCCR1C = 0x00;
	while (1)
	{
		/* Turn LED on. */
		led_set (LED1, 1);
		/* Initialise the counter */
		TCNT1 = 0;
		/* wait for 500 milliseconds. */
		while (TCNT1 < DELAY_TICKS){}
		/* Turn LED off. */
		led_set (LED1, 0);
		/* Reset the timer*/
		TCNT1 = 0;
		/* wait for 500 milliseconds. */
		while (TCNT1 < DELAY_TICKS){}
	}
}
```