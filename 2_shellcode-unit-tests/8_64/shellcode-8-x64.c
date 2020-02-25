#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
	char buf0[2];
	int t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15;

	t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = t10 = t11 = t12 = t13 = t14 = t15 = 0xdead;

	printf("Stack Infoleak: %p\n", buf0);

	fgets(buf0, 83, stdin);

	if ((t0 == t1) && (t2 == t3) && (t4 == t5) && (t6 == t7) && (t8 == t9) && (t10 == t11) && (t12 == t13) && (t14 == t15) && (t15 == 0xdead))
	{
		puts("Bring the broken back to life.");
	}

}

void main(void)
{
	vuln();
}
