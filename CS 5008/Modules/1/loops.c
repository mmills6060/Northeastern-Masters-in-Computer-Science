#include <stdio.h>

int main(){
    int counter = 0;

    while ( counter < 5) {
        printf("%d ", counter);
        counter = counter + 1;
    }

    printf("\n");

    for(int i = 0; i < 5; i = i + 1) {
        printf("%d ", i);
    }
    printf("\n");
   return 0;
}