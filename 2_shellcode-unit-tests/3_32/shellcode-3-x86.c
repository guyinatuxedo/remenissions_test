#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf1[100];
	char buf0[100];
	printf("Stack Infoleak: %p\n", buf0);
	gets(buf1);
}

void main(void)
{
	vuln();
}
