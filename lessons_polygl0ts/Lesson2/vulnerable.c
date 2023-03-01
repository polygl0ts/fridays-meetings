#include <stdio.h>
#include <stdlib.h>

void win() {
    system("/bin/sh");
}

void vulnerable() {
    char respect[50];
    fgets(respect, 2000, stdin);
    return;
}


int main () {
    vulnerable();
}
