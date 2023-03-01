#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void win() {
    system("/bin/sh");
}

void vulnerable() {
    char buffer[20];
    printf("Please give me your name\n");
    read(0, buffer, 100);
    printf("Your name is %s\n", buffer);
    printf("Give me the name of your friend!\n");
    read(0, buffer, 100);
    printf("Your friend's name is %s\n", buffer);
    return;
}

int main () {
    vulnerable();
}
