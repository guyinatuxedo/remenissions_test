#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void pwned(void)
{
	system("/bin/sh");
}

void main(void)
{
	char printBuf[250];
	char buf[100];


	fgets(buf, sizeof(buf), stdin);

	strcpy(printBuf, "01234");
	strncpy(printBuf + 5, buf, sizeof(buf));

	printf(printBuf);

	fflush(stdin);
}
