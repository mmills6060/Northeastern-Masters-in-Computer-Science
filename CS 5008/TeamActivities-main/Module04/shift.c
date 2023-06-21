#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int x = atoi(argv[1]);
    int shifted = (x << 5) + x;
    printf("%d << 5 + x = %d\n", x, shifted);
    int shifted2 = x * 32 + x;
    printf("%d * 32 + x = %d\n", x, shifted2);
    int shifted3 = x * 33;
    printf("%d * 33 = %d\n", x, shifted3);
    return 0;
}
