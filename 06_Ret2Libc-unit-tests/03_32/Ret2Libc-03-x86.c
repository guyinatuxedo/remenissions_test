#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf0[20];

	printf("I live to fight another: %p\n", printf);
	fgets(buf0, 0x30, stdin);
}

void main(void)
{
	vuln();
}
