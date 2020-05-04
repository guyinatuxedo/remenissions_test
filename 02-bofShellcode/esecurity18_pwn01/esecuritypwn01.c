#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
  char buffer[32];
  printf("DEBUG: %p\n", buffer);
  gets(buffer);
}

