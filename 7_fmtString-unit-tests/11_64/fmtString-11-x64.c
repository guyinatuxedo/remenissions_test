#include <stdio.h>
#include <stdlib.h>

void main(void)
{
	char buf[100];
	int v0, v1, v2;

        printf("It seems I've been buried alive: %p\n", printf);

	fflush(stdin);

	fgets(buf, sizeof(buf), stdin);

	printf(buf);

	fflush(stdin);
}