#include <stdio.h>
#include <stdlib.h>

void win(void)
{
	system("/bin/sh");
}

void vuln(void)
{
	char vuln[20];
	int var0;
	fgets(vuln, 100, stdin);

	if (var0 != 0xfacade)
	{
		exit(0);
	}

}

void main(void)
{
	vuln();
}
