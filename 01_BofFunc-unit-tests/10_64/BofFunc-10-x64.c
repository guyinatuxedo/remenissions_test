#include <stdio.h>
#include <stdlib.h>

void win(void)
{
	system("/bin/sh");
}

void vuln(void)
{
	char vulnBuf[20];
	int var0, var1, var2;
	long var3;

	printf("We're dreaming in color: %p\n", vuln);

	fgets(vulnBuf, 100, stdin);

	if (var0 != 0xfacade)
	{
		exit(0);
	}

	if (var1 != 0xdead)
	{
		exit(0);
	}

	if (var3 != 0xdeadbeefdeadbeef)
	{
		exit(0);
	}

}

void main(void)
{
	vuln();
}
