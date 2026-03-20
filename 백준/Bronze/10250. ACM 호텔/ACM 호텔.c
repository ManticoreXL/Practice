#include <stdio.h>

int main(void) {

    int t, h, w, n;
    int floor, number, room;

    scanf("%d", &t);

    for(int i = 0; i < t; i++) {
        scanf("%d %d %d", &h, &w, &n);

        floor = (n % h == 0) ? h : (n % h); 
        number = (n % h == 0) ? (n / h) : (n / h + 1); 
        room = floor * 100 + number;

        printf("%d\n", room);
    }

    return 0;
}