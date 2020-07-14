#include <stdio.h>
#include <stdlib.h>

void notPwned(void)
{
	system("/bin/ls");
}

void main(void)
{
	char buf[150];
	int v0, v1, v2;

        printf("It seems I've been buried alive: %p\n", printf);


	fgets(buf, sizeof(buf), stdin);

	printf(buf);

	exit(0);
}
