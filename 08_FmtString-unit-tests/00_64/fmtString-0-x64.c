#include <stdio.h>
#include <stdlib.h>


void pwned(void)
{
	system("/bin/sh");
}

void main(void)
{
	char buf[100];

	fgets(buf, sizeof(buf), stdin);

	printf(buf);

	fflush(stdin);
}
