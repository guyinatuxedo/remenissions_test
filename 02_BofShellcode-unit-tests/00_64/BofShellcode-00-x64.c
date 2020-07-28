#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf[100];

	printf("Stack Infoleak: %p\n", buf);
	gets(buf);
}

void main(void)
{
	vuln();
}
