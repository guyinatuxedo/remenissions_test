#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf0[2];
	char buf1[2];
	

	printf("Stack Infoleak: %p\n", buf1);

	fgets(buf0, 124, stdin);
}

void main(void)
{
	vuln();
}
