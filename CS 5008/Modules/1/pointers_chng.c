#include <stdio.h>

void update(int* argument){
    *argument = 10;
}

int main(){
    int value = 5;
    int* p_value = &value;

    update(p_value);

//    printf("value is: %d\n", value);
//    printf("the address of value is: %p\n", p_value);
//    printf("The value at p_value is: %d\n", *p_value);
//    update(value);

    printf("value updated is: %d\n", value);
    return 0;
}