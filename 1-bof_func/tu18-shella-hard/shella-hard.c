// gcc -o shella-hard shella-hard.c -m32 -no-pie -fno-pic -mpreferred-stack-boundary=2
#include <unistd.h>

void giveShell();

void main()
{
  char buf[0x10]; // [sp+0h] [bp-10h]@1

  read(0, buf, 0x1Eu);
}

void giveShell()
{
//    asm("nop\n"
//        ".byte 0xa1\n");
    execve("/bin/sh", 0, 0);
}
