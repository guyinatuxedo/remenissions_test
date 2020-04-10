#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void pwned(void)
{
	system("/bin/sh");
}

void main(void)
{
	char buf[100];
	char printBuf[244];



	fgets(buf, sizeof(buf), stdin);

	sprintf(printBuf, "Throw ourselves:%s", buf);

	printf(printBuf);

	fflush(stdin);
}
