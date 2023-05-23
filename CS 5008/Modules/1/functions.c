#include <stdio.h>
void foo(int arg1){
    printf("From foo: %d\n", arg1);
}

int sum(int a, int b){
    return a + b;
}

void bar();

int main(){
     foo(23);
     bar();       
   return 0;
}

void bar(){
    int num1 = 5;
    int num2 = 6;
    int result = sum(num1, num2);
    printf("%d + %d = %d\n", num1, num2, result);

}