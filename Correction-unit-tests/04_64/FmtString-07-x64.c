#include <stdio.h>
#include <stdlib.h>

void notPwned(void)
{
	system("/bin/ls");
}

void main(void)
{
	char buf[100];
	int v0, v1, v2;

        printf("it seems i've been buried alive: %p\n", printf);
        printf("Cancelled out and rendered obsolute: %p\n", main);

	fgets(buf, sizeof(buf), stdin);

	printf(buf);

	exit(0);
}
