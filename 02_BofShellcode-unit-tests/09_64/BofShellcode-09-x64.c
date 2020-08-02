#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf[100];

	printf("A Dark Sun: %p\n%p\n", buf, vuln);
	gets(buf);
}

void main(void)
{
	vuln();
}
