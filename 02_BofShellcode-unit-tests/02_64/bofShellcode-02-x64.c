#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf[100];

	printf("Stack Infoleak: %p\n", buf);
	scanf("%s", buf);
}

void main(void)
{
	vuln();
}
