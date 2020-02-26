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
	int target0, target1;
	char buf1[200];

	fgets(buf0, 100, stdin);

	if (target1 == 0xdead)
	{
		exit(0);
	}

	if (target0 == 0xfacade)
	{
		ptr();
	}
}
