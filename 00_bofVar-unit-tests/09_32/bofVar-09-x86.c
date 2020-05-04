#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main(int argc, char *argv[])
{
	char buf[50];
	int target;

	strcpy(buf, argv[1]);

	if (target == 0xfacade)
	{
		puts("flag{I'm burning inside}");
	}
}
