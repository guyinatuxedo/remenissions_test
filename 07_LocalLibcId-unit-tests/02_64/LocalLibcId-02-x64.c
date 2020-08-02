#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf[50];
	int var0;

	printf("Silence in the Snow!\n");
	fgets(buf, 200, stdin);
	if (var0 != 0xdeadbeef)
	{
		exit(0);
	}
}

void main(void)
{
	vuln();
}
