#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf[10];
	int t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14;
	

	printf("Stack Infoleak: %p\n", buf);

	t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = t10 = t11 = t12 = t13 = t14 = 0xdead;


	fgets(buf, 124, stdin);


	if ((t0 != 0xfacade) && (t14 != 0xfacade))
	{
		exit(0);
	}
}

void main(void)
{
	vuln();
}
