#include <stdint.h>
#include <stdio.h>



typedef struct {
    uint32_t id;
    uint8_t age;
    float gpa;
} Student;

Student newStudent(uint32_t id, uint8_t age, float gpa)
{
    Student stud = {id, age, gpa};
    return stud;
}

void printStudent(const Student* student)
{
    printf("%d: Age %d, GPA %.2f\n", student->id, student->age, student->gpa);
}

void updateGpa(Student* student, float newGpa)
{
    student->gpa = newGpa;
}

int main()
{
    Student student = newStudent(12345678, 19, 5.62);
    printStudent(&student);
    updateGpa(&student, 6.2);
    printStudent(&student);
}