#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln(void)
{
        char buf[500];

	memset(buf + 512, 0x0, 0xc);

        fgets(buf, sizeof(buf), stdin);

	strncpy(buf + 512, buf + 512, 10);

        printf(buf);

	exit(0);
}

void main(void)
{
	vuln();
}
