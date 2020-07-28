  
#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf0[20];

	printf("I live to fight another: %p\n", printf);
	gets(buf0);
}

void main(void)
{
	vuln();
}
