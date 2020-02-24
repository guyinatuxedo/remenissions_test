#include <stdio.h>
#include <stdlib.h>

void main(void)
{

	char buf[50];

	int target0, target1, target2, target3, target4, target5;

	target2 = 0xdead;

	fgets(buf, 100, stdin);

	if ((target0 == 0xfacade) && (target1 != 0xbeef) && (target2 < 0xdead) && (target3 > 0xfacade) && (target4 <= 0xbeef) && (target5 >= 0xdead))
	{
		system("/bin/sh");
	}

}
