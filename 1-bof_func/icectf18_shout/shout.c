#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

void shell() {
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    system("/bin/sh -i");
}

void message(char *input) {
    char buf[16];
    strcpy(buf, input);

    printf("The cave echoes.. %s\n", buf);
}

int main(int argc, char **argv) {
    if (argc > 1){
        message(argv[1]);
    } else {
        printf("Usage: ./shout <message>\n");
    }
    return 0;
