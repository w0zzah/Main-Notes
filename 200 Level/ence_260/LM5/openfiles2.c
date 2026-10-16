#include <stdio.h>
#include <ctype.h>

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

FILE* openInputFile(const char* filename)
{
    FILE* file = fopen(filename, "r");

    if (file == NULL) {
        printf("Input file can't be opened\n");
    }
    
    return file;
}

FILE* openOutputFile(const char* filename)
{
    FILE* file = fopen(filename, "w");

    if (file == NULL) {
        printf("Output file can't be opened\n");
    }

    return file;
}

int main(void)
{
    char inputFilename[81];
    char outputFilename[81];

    FILE* inputFile;
    FILE* outputFile;

    int character;
    int afterWhitespace = 1;

    readString(inputFilename, 80);
    readString(outputFilename, 80);

    inputFile = openInputFile(inputFilename);
    outputFile = openOutputFile(outputFilename);

    if (inputFile == NULL || outputFile == NULL) {
        if (inputFile != NULL) {
            fclose(inputFile);
        }
        if (outputFile != NULL) {
            fclose(outputFile);
        }
        return 0;

        
    }

    while ((character = getc(inputFile)) != EOF) {

        if (isspace(character)) {
            putc(character, outputFile);
            afterWhitespace = 1;
        } else {
            if (afterWhitespace) {
                character = toupper(character);
                afterWhitespace = 0;
            } else {
                character = tolower(character);
            }

            putc(character, outputFile);
        }
    }

    fclose(inputFile);
    fclose(outputFile);

    return 0;
}