#include <stdio.h>
#include <stdlib.h>

void win(void)
{
	system("/bin/sh");
}

void vuln(void)
{
	char vulnBuf[20];
	int var0;

	printf("Stop drop and roll: %p\n", vuln);

	fgets(vulnBuf, 100, stdin);

	if (var0 != 0xfacade)
	{
		exit(0);
	}

}

void main(void)
{
	vuln();
}
