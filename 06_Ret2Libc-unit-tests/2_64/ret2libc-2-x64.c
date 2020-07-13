#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf0[20];
	int target;

	printf("I live to fight another: %p\n", printf);
	gets(buf0);
	if (target != 0xfacade)
	{
		exit(0);
	}
}

void main(void)
{
	vuln();
}
