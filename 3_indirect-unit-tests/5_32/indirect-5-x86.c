#include <stdio.h>
#include <stdlib.h>


void notPwn0(void)
{
	exit(0);
	system("/bin/sh");
}

void pwn(void)
{
	system("/bin/sh");
}

void notPwn1(void)
{
	exit(0);
	system("/bin/sh");
}

void main(void)
{

	char buf0[20];
	volatile int (*ptr0)();
	volatile int (*ptr1)();
	volatile int (*ptr2)();
	char buf1[200];
	int v0, v1;

	fgets(buf0, 100, stdin);

	if (v0 == 0xdead)
	{
		ptr0();
	}

	if (v0 == 0xdead)
	{
		ptr2();
	}

	ptr1();

}
