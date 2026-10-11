
## Init pins
- **DDRx** = Data Direction
- **PORTx** = Output data
- **PINx**  = Input regis
## Controlling Pins:

- **Setting a pin (Set to 1):** PORTC = PORTC | (1<<2); or PORTC |= (1<<2);
- **Clearing a bit (Set to 0):** PORTC &= ~(1<<2);
- **Toggling a bit (Changes value):** PORTC ^= (1<<2);
- **Testing a bit (return 1 if bit is set):** if ((PINC & (1<<2)) != 0)

## Define Macro
**#define BIT(X) (1<<X)**
 - This macro has a single argument x which the preprocessor subs


#### Lab 1

1. **Set Pin 2 as output:**

```c
#include <avr/io.h>
int main (void)
{
	system_init ();
	/* Set PIN 2 as an output port to drive LED 1. */
	DDRC != (1 << 2);
	while (1)
	{
	/* Turn LED 1 on. */
	}
}
```