#include <stdio.h>
#include <stdlib.h>

void main(void)
{

	char buf0[50];
	volatile int (*ptr)();
	char buf1[200];

	printf("What the dead men say: %p\n", buf0);

	fgets(buf0, 100, stdin);

	ptr();

}
