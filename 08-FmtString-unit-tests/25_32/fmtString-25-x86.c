#include <stdio.h>
#include <stdlib.h>

void main(void)
{
	char buf[100];
	int i;

	fgets(buf, sizeof(buf), stdin);

	printf(buf);

	fflush(stdin);

}
