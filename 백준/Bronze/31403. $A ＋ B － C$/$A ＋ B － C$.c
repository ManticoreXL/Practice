#include <stdio.h>

int main(void) {

    int a, b, c;

    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);

    // number
    printf("%d\n", a + b - c);

    // string
    if (b == 1000)
        a *= 10000;
    else if (b >= 100 && b < 1000)
        a *= 1000;
    else if (b >= 10 && b < 100)
        a *= 100;
    else
        a *= 10;

    printf("%d\n", a + b - c);

   return 0;
}