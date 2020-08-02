#include <stdio.h>
#include <stdlib.h>


void print(void)
{
	puts("The beauty in the sorrow.");
}

void vuln(void)
{
	char buf[50];

	gets(buf);
}

void main(void)
{
	vuln();
}
