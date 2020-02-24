#include <stdio.h>
#include <stdlib.h>

void main(void)
{

	char buf[50];

	int target0;
	long target1;
	int target2;

	target2 = 0xdead;

	fgets(buf, 100, stdin);

	if ((target0 == 0xfacade) && (target1 == 0xbeef) && (target2 != 0xdead))
	{
		system("/bin/sh");
	}

}
