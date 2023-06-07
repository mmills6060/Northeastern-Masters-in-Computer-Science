#include <stdio.h>

struct student {
    double creditHours;
    int age;
    int id;
};

struct student makeStudent(int id, int age, double creditHours){
    struct student tempStudent;
    tempStudent.id = id;
    tempStudent.age = age;
    tempStudent.creditHours = creditHours;
    return tempStudent;
}

void printStudent(struct student aStudent){
    printf("%d %d %f\n", aStudent.id, aStudent.age, aStudent.creditHours);
}
int main(){
    struct student s1 = makeStudent(1001, 23, 12.5);
    struct student s2;
    s2.id = 1002;
    s2.age = 24;
    s2.creditHours = 13;
    printStudent(s1);

    printf("%d %d %f\n", s2.id, s2.age, s2.creditHours);
   return 0;
}