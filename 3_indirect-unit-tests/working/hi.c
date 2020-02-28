#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char hi[100];

	printf("like breathing in sulfur: %p\n", hi);
	gets(hi);
	puts(hi);
}

void main(void)
{
	vuln();
}
