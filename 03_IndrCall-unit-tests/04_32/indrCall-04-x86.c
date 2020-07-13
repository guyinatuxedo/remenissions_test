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

	fgets(buf0, 100, stdin);

	if (ptr == 0xdead)
	{
		exit(0);
	}

	else if (ptr != 0x0)
	{
		ptr();
	}

}
