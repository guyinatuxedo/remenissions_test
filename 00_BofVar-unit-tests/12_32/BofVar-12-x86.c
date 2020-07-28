#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main(int argc, char ** argv)
{

	char buf[50];
	int target0;

	strncpy(buf, argv[1], 64);
	printf("Input is: %s\n", buf);

	if (target0 == 0xfacade)
	{
		system("cat flag.txt");
	}
}
