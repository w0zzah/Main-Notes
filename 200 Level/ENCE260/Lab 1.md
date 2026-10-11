
### LED's
**Initialise led**
```c
static void led_init (void)
{
	/* Set led port to be an output */
	DDRC |= (1 << 2)
}
```
**Set up the led on function**
```c
static void led_on (void)
{
	/* Set led port output */
	PORTC |= (1 << 2);
}
```
**Set up the led off function**
```c
static void led_init (void)
{
	/* Set led port output off */
	PORTC &= ~(1 << 2);
}
```

### Buttons

**Initialise button for input**
```c
static void button_init (void)
{
	/* Set pin 7 of port D to input:(zero) */
	DDRD |= (0 << 7);

	/* Set button pin status in bit 7 of the port register*/
	PORTD |= (0 << 7);
}
```

**Set on pressed function**

```c
static int button_pressed_p (void)
{
	/* Check if the state of the button has changed */
	if ((PIND & (1 << 7)) != 0) {
		/* return no zero if the button has been presed*/ 
		return true;
	} else {
		return false;
	}
}
```


### Linking .h through make file

```c
# Compile: With single c file
lab1-ex2.o: lab1-ex2.c ../../drivers/avr/system.h /* Here 1 file*/
$(CC) -c $(CFLAGS) $< -o $@  
system.o: ../../drivers/avr/system.c ../../drivers/avr/system.h
$(CC) -c $(CFLAGS) $< -o $@
```

```c
# Compile: Linking other .h files
lab1-ex3.o: lab1-ex3.c ../../drivers/avr/system.h button.h led.h /* Link h file*/
$(CC) -c $(CFLAGS) $< -o $@
system.o: ../../drivers/avr/system.c ../../drivers/avr/system.h
$(CC) -c $(CFLAGS) $< -o $@
button.o: button.c button.h /* Link button c + h files*/
$(CC) -c $(CFLAGS) $< -o $@
led.o: led.c led.h          /* Link led c + h files*/
$(CC) -c $(CFLAGS) $< -o $@
```


### Using a port I/O Module


**Configure a LED**
```c
#include "pio.h"
#define LED_PIO PIO_DEFINE (PORT_C, 2) /* (macro to the port, bit/pin no.)*/ 

int main (void)
{
	pio_config_set (LED_PIO, PIO_OUTPUT_LOW); /* Set DDR to be out*/
	while (1)
	{
		pio_output_low (LED_PIO);
		pio_output_high (LED_PIO);
	}
 return 0;
}
```

**Configure a Button**
```sql
#include "pio.h"
#include "button.h"
#define BUTTON_PIO PIO_DEFINE (PORT_D, 7)
static int state = 0;

/** Checks state when button is pressed to see  */
int button_pressed_p (void)
{
	int current_state = pio_input_get(BUTTON_PIO);
	
	if (current_state && (state == 0)) {
		state = 1;
		return 1;
	}
	if (current_state && (state == 1)) {
		state = 0;
		return 0;
	}
}
/** Initialise button1. */
void button_init (void)
{
	pio_config_set (BUTTON_PIO, PIO_INPUT);
}
```