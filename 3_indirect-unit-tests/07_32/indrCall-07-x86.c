#include <stdio.h>
#include <stdlib.h>


void pwn(void)
{
	system("/bin/sh");
}

void main(void)
{

	char buf0[20];
	volatile int (*ptr0)();
	volatile int (*ptr1)();
	volatile int (*ptr2)();
	char buf1[200];
	int v0, v1, v2;

	fgets(buf0, 100, stdin);

	if (v0 == 0xdead)
	{
		exit(0);
		ptr0();
	}

	else if (v1 == 0xbeef)
	{
		exit(0);
		ptr1();
	}

	else if (v2 == 0xfacade )
	{
		if (ptr1 != 0)
		{
			ptr2();
		}
	}


}
