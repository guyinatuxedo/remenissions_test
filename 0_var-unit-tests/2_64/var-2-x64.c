#include <stdio.h>
#include <stdlib.h>

void main(void)
{

	char buf[50];

	int t0, t1, t2, t3, t4, t5;

	fgets(buf, 100, stdin);

	if ((t0 > 0xdead) && (t1 < 0xdead) && (t2 >= 0xfacade) && (t3 <= 0xfacade) && (t4 == 0xbeef) && (t5 == 0xbeef))
	{
		system("/bin/sh");
	}

}
