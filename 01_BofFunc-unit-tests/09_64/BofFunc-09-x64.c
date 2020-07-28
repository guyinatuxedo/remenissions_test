#include <stdio.h>
#include <stdlib.h>

void win(void)
{
	system("/bin/sh");
}

void main(void)
{
	char vuln[20];
	int var0;

	printf("The preservation of the martyr in me: %p\n", main);
	fgets(vuln, 100, stdin);
	

	if (var0 != 0xfacade)
	{
		exit(0);
	}


}
