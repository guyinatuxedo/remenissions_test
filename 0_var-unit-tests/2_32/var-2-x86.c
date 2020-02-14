#include <stdio.h>
#include <stdlib.h>

void main(void)
{

	char buf[50];

	int target0, target1;

	fgets(buf, 54, stdin);



	if (target1 == 0xdead)
	{
		puts("rip");
		exit(0);
	}

	if (target0 == 0xfacade)
	{
		system("/bin/sh");
	}

}
