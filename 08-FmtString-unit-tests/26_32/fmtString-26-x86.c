#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln(void)
{
        char buf[500];

	memset(buf + 500, 0x0, 30);

        fgets(buf, sizeof(buf), stdin);

	strncpy(buf + 500, buf + 500, 10);

        printf(buf);

	exit(0);
}

void main(void)
{
	vuln();
}
