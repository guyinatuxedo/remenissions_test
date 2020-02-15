#include <stdio.h>
#include <stdlib.h>

void main(void)
{
	char buf0[50];	
	int t0, t1, t2, t3, t4, t5;
	char buf1[50];

	fgets(buf0, 70, stdin);

	if (t0 == 0xdead)
	{
		if (t1 != 0xbeef)
		{
			exit(0);
		}

		else if (t2 == 0xfacade)
		{
			system("/bin/sh");
		}
	}
}