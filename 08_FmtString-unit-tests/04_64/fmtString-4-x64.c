#include <stdio.h>
#include <stdlib.h>


void pwned(void)
{
	system("/bin/sh");
}

void main(void)
{
	char buf[100];

	printf("We're dreaming: %p\n", main);

	fgets(buf, sizeof(buf), stdin);

	printf(buf);

	fflush(stdin);
}
