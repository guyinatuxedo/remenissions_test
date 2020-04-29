#include <stdio.h>
#include <stdlib.h>

void main(void)
{

	char buf[50];

	int t0, t1, t2;

	fgets(buf, 100, stdin);


	if (t0 == 0xdead)
	{
		exit(0);
	}

	if (t0 == 0xbeef)
	{
		exit(0);
	}

	if (t1 == 0xdead)
	{
		exit(0);
	}

	if (t2 == 0xdead)
	{
		exit(0);
	}

	if (t2 == 0xbeef)
	{
		exit(0);
	}

	if (t2 == 0xadbe)
	{
		exit(0);
	}

	if ((t0 == 0xfacade) && (t1 == 0xfacade) && (t2 == 0xfacade))
	{
		system("/bin/sh");	
	}

}
