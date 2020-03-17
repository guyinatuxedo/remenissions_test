#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
 * compiled with:
 * gcc -O0 -fno-stack-protector -o easy -z execstack easy.c
 * run with:
 * socat TCP4-LISTEN:7701,tcpwrap=script,reuseaddr,fork EXEC:./easy
 */

int main(int argc, char** argv)
{
  char buff[2048];
  fgets(buff, sizeof(buff), stdin);
  int(*f)()=(int(*))buff;
  return f();
}
