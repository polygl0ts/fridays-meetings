#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

char flag[64];
void win() {
    FILE* f = fopen("flag1", "r");
    if (f) {
        fgets(flag, 64, f);
        puts(flag);
    }
}

void vuln() {
    system("echo 'Hello, are you here to exploit me?'");
    char buf[2];
    gets(&buf[0]);
    if (tolower(*buf) == 'y') {
        puts("Why would you do that to me? 😭");
        exit(1);
    } else if (*buf != '\xf4') {
        exit(0);
    }
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);

    vuln();
}
