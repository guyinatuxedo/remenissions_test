#include <stdio.h>
#include <stdlib.h>


void pwn(void)
{
	system("/bin/sh");
}

void main(void)
{

	char buf0[20];
	volatile int (*ptr)();
	char buf1[200];

	printf("Don't live your life in shame: %p\n", printf);
	fgets(buf0, 100, stdin);

	ptr();

}
