#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * compiled with:
 * gcc -O0 -fno-stack-protector -o hard -z execstack hard.c 
 * run with:
 * socat TCP4-LISTEN:7703,tcpwrap=script,reuseaddr,fork EXEC:./hard
 */

int main(int argc, char *argv[])
{
    char buf[1024];
    fscanf(stdin, "%s", &buf);
    int(*f)()=(int(*))buf;
    return f();
}

