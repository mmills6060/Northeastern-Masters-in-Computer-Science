#include <stdio.h>

int main(){
    int accountId = 5;
    double accountBalance = 100.53;
    char accountType = 'C';
    printf("AccountID  is: %d\n", accountId);
    printf("AccountBalance is: %f\n", accountBalance);
    printf("AccountTY is: %c\n", accountType);
   // return the the size of each variable in bytes 
   printf("sizeof(int): %d\n", sizeof(int)); 
   printf("sizeof(double): %d\n", sizeof(double)); 
   printf("sizeof(char): %d\n", sizeof(char)); 
    return 0;
}