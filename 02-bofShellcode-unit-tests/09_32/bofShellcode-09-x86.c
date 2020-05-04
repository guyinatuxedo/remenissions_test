#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf[100];

	printf("A Dark Sun: %p %p\n", vuln, buf);
	gets(buf);
}

void main(void)
{
	vuln();
}
