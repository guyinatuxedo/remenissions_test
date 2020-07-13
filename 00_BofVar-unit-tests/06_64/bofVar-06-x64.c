#include <stdio.h>
#include <stdlib.h>

void main(void)
{

	char buf[50];

	int target0;

	fgets(buf, 100, stdin);


	if (target0 == 0xdead)
	{
		exit(0);
	}

	else if (target0 == 0xfacade)
	{
		system("/bin/sh");
	}
}
