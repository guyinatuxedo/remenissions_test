#include <stdio.h>
#include <stdlib.h>

void win(void)
{
	system("/bin/sh");
}

void vuln(void)
{
	char vuln[20];
	int var0, var1, var2, var3;

	fgets(vuln, 100, stdin);

	if (var0 != 0xfacade)
	{
		exit(0);
	}

	if (var1 != 0xdead)
	{
		exit(0);
	}

	if (var3 != 0xdeadbeef)
	{
		exit(0);
	}

}

void main(void)
{
	vuln();
}
