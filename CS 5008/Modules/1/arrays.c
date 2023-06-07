#include <stdio.h>

int main(){
    int array[3] = {1, 2, 3};
    /*array[0] = 0;
    array[1] = 1;
    array[2] = 2;
    */
    for ( int i = 0 ; i < 3 ; i = i + 1) {
        printf("%d ", array[i]);
    }
   return 0;
}