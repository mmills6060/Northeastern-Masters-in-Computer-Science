#include <stdio.h>
typedef struct student {
    int id;
    int age;
}student_t;

void printStudent(student_t* astudent){
    printf("%d %d\n", astudent->id, (*astudent).age);
}

void updateStudent(student_t* astudent, int age, int id){
    (*astudent).id = id;
    (*astudent).age = age;
}
int main(){
    student_t s1;
    student_t s2;
    // lets assign values to the fields of s1
    updateStudent(&s1, 23, 1001);
    updateStudent(&s2, 24, 1002);
   
    s2.id = 1002;
    s2.age = 24;

    printStudent(&s1);
    printStudent(&s2);

    s2.id = 1003;

    printStudent(&s2);
    printf("s1.id = %d\n", s1.id);
    printf("s1.age = %d\n", s1.age);
   return 0;
}