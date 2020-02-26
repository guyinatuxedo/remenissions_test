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

	printf("To the right I can see a church: %p\n", main);

	fgets(buf0, 100, stdin);

	ptr();

}
