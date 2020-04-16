#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(void)
{
	char buf[100];
	char misc[20];

	fgets(buf, sizeof(buf), stdin);

	strncpy(misc, (char *)printf, 10);

	printf(buf);

	exit(0);
}
