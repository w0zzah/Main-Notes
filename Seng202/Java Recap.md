### Class's
- A class is used for most objects in java.
```Java
import java.// Required imports

public class ClassName  { // make sure its the same name as the file
	// Define variable's
	// Visibility Type Name 
	private int number;
	
	// Constructor TIP: After writing out variables, right click in intellij -> 
	// Generate -> Constructor
	ClassName(int number) {
	this.number = number;
	}
	
	// Functions
	// Visibility returnType FuncName() {}
	public void classFunc() {
		// function
	}
}
```

### Enums
- Enums are useful for when we need to represent an entities state. These states can also carry additional information or store additional information. e.g A computer has states 'on, off, sleeping, hibbernating' each with a wattage '100, 0, 5, 2' respectively. This works well with switch statements when we need to switch between each state based off of a variable.
	[docs]([https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html))

```java
public enum enumName {
	state1(var1, var2),
	state2(var1, var2),
	state3(var1, var2);
	
	public final type var1;
	public final type var2;
	
	enumName(type var1, type var2) {
		this.var1 = var1
		this.var2 = var2
	}
}
```


### For-Loops
- For -> Looping -> Lmao
[docs](https://www.baeldung.com/java-for-each-loop)
```Java
int intial = 0;
bool condition = initial < var.size();
increment = intial + x

for (intial; condition; increment) {
	// Add function, each loop initial increases by increment
}
```

