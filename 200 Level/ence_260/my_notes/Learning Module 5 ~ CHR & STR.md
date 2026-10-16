Any set of obj can be assigned a unique encoding value, such as Apple as 1 and Orange as 2. We can use an enum to construct these sets. There doesnt need to be any particular order to the set it is not important to consider operators less than orgrater than. However some sets may have a natural ordering like the alphabet so in construction order is important.


#### Char:
- **char** is a special type of 8-bit integer . its special because it is encoded as a number but should be treated as just a character from the ASCII table. The char is a fundamental type so its a symbol encapsulated within the single quotes '' will be converted into its corresponding ASCII int value, E.g
- **char** aCharacter = 'c';
- Alternatively you can also directly assign an integer value to a char and when it is printed as a character the corresponding ASSCII typographical symbol will be used. finally, note that a character given in a single quote form that has a slash followed by a num e.g '\1115' is yet another way of specify the octal value, Octals can also be specified with quotes by using a leading zero


### ASCII Values:
- We use 8-bit as ASCII Sencompasses 26 lower case + upper case symbols, plus the bumber symbols and some typographic symbols such as ! and ,. Special symbols like TAB and SPACE are also included. this brings the total to 127 total different symbols.
- ASCII can be represented in 5 distinct ways

| Char  | Normal | '\oct' | 0oct | Dec | Hex  |
| ----- | ------ | ------ | ---- | --- | ---- |
| Space | ' ';   | '\40'  | 040  | 32  | 0x20 |
### Strings:
- A string is a simple array of chars, where we establish the length of the string first where the last character of the array si given as '\0' The additional character is called the null-character and is counted in terms of array length
- The Null-Character is important as its used to signal the end of the string allowing it to have a variable length however this implies that the length of array(n), can hold at most N-1 charcters.
##### E.G: char aString[20] = {'A', 0x20, 'B', 32, ... '\0' } 
### String Literals
- C also permits Strings encapsulated in the double quote e.g "A string" Which is converted into an array of characters with a terminating nuldl char and allocated into the global space of memory as a read only const char*. When the string literal is used, it is replaced by the address in memory where the string is allocated. 
Consider this declaration: **char* anotherString = "A String"**

### Care:
- Because of the way a string is constructed we cant use the sizeof() function to find the string length as it will only tell you the maximum str len. Instead we use **strlen()** function. If trying to print(*char string[20] = "20characters";*) then instead of placing a \0 at the end, the compiler sets the [20] as "s" -> then when **printf** is calledm the printf just goes to the very next byte in memory till it reaches 0x00

### Reading From STD input:

#### Reading a Char:
```c
scanf("%d", &a);             // read a single integer into a
scanf("%d %d", &a, &b);       // read two integers into a, b respectively
scanf("%f", &f);             // read a float, into f
scanf("%c", &c);             // read a character, into c.Note,  newline is a chr 
```

- We often use chars such as TAB and newline to seperate indivdual tokes and the %format translator is used t otransform the token into the right sort of value if the token is of the wrong format then the token is ignored until the right token is found. 
#### Reading a String:
```c 
char a[BUFFER_SIZE];
scanf("%s", &a);              // read a string
```

- If the input Hello World was given then a will only be Hello as the white space breaks the token. scanf function assumes that the programmer has allocated a character array buffer bug enough to fit the null char terminated string(token)is going to return. But this is ripe for error as the programmer has little to no control on the user who will enter the string. This makes scanf() vulnerable t obuffer-overflow errors. **Do not use scanf to read a string**
#### EOF ~ End Of File
- When reading a file, incl from std input, we often need to know when we have reached the end of the file, this can be called with EOF
- If you look at  the getchar() func, you will notice that it returns not a char type but an int type. The integer data type is convenient because we can use the larger size to return useful info if the function fails, If unsuccessful Instead of returning a character the getchar() returns a negative number Identifying how it failed. EOF is one such exception idicating there are no more characters to read.


# Files:
- It would be useful to be able to open ordinary files, and the read/write them the same way we do with standard input and output. The C standard library provides a file type, FILE, which supports vairants of printf() and scanf()
- In the UNIX enviroment everything is a file, the keyboard(std user input), the screen(std user output), memory, network connections, as well as your standard files on the disk. Each sort of device or onkect might have its own specialised function to open them, but from there on the functionality is the same. They can all be interfaced with the same func. It is only possible because the operating system maintains a mechanism for managing file indices and a common API that device driver programmers must follow. 
#### How we interact with them?

#### fopen() 
- Is used to open a file. You must specify a filename and a mode, both of which are strings. 
	- "r" is to open for reading
	- "w" for writing/overwriting
	- "a" to append (write at the end of the file)
	- "b" can be specified if the file is binary.

	```c
	FILE* aFile;
	char filename[] = "example.txt";
	char mode[] = "r";
	aFile = fopen(filename, mode);
	```

##### fclose():  
- The fclose() function  is used to close a file, that you should have opened first. While files will automatically be closed when the program terminates, it is best practice to do this yourself and as soon as practical after having finished using it. Closing a file will cause it to sunc, meaning any cached buffers will be cleared.
```c
FILE* aFile;
//...
fclose(aFile)
```

#### fprintf()
- Takes the file pointer as it's first parameter then writes data to the file.
```c
fprintf(aFile, "Some data: %d\n", data)
```
#### fscanf()
- Takes the files pointer and reads the data
```c
fscanf(aFile, "%d\n", &data);
```

#### Question 8:

Write a program that reads a filename and a character from std input. the program should then open the file and counts how many times the character appears in the file, printing this value to a std out. Filenames will be amaximum of 80 characters in length.

**Key Functionality:** 
- *FILE\* openInputFile(char\* filename)* That ioebs the input file and returns its file pointer obect. The function should print "Inpout file can't be opened" if the file fails for some reason.
- If the input file can't be opened (i.e openInputFile() returns NULL) exit
- Otherwise, count the number of times the character specified by the user appears in the file, and print the total. Make sure to close the input file when you're done

#### COMPLETED CODE
```c
#include <stdio.h>

size_t readString(char* string, size_t maxStringLength)
{
    size_t count = 0;
    int character;

    while (count < maxStringLength && (character = getchar()) != '\n' && character != EOF) {
        string[count] = (char)character;
        count++;
    }

    string[count] = '\0';

    return count;
}

FILE* openInputFile(char* filename)
{
    FILE* file = fopen(filename, "r");

    if (file == NULL) {
        printf("Input file can't be opened\n");
    }

    return file;
}

int main(void)
{
    char filename[81];
    char character;
    FILE* file;
    int count = 0;
    int c;

    readString(filename, 80);

    character = getchar();

    file = openInputFile(filename);

    if (file == NULL) {
        return 0;
    }

    while ((c = getc(file)) != EOF) {
        if (c == character) {
            count++;
        }
    }

    printf("%d\n", count);

    fclose(file);

    return 0;
}
```