#include <stdio.h>
#include <stdlib.h>

void main(void)
{

	char buf[50];
	int target0;

	fscanf(stdin, "%s", buf);
	printf("Input is: %s\n", buf);

	if (target0 == 0xfacade)
	{
		system("cat flag.txt");
	}
}
