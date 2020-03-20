#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf[50];


	printf("Silence in the Snow!\n");
	gets(buf);
}

void main(void)
{
	vuln();
}
