#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf[50];


	puts("I fight another\n");
	printf("Endless Night: %p\n", buf);
	gets(buf);
}

void main(void)
{
	vuln();
}
