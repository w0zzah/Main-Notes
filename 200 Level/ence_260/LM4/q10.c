#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int32_t id;
    int32_t age;
    float gpa;
} Student;

Student newStudent(uint32_t id, uint8_t age, float gpa)
{
    Student new;
    new.id = id;
    new.age = age;
    new.gpa = gpa;
    return new;
}

void printStudent(const Student* student)
{
    printf("%u: Age %u, GPA %.2f\n", student->id, student->age, student->gpa); 
}

void updateGpa(Student* student, float newGpa)
{
    student->gpa = newGpa;
}


int main(void) {
Student student = newStudent(12345678, 19, 5.62);
printStudent(&student);
updateGpa(&student, 6.2);
printStudent(&student);
}