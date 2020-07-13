#include <stdio.h>
#include <stdlib.h>


void vuln(void)
{
        char buf[500];

        fgets(buf, sizeof(buf), stdin);

        printf(buf);

	exit(0);
}

void main(void)
{
	vuln();
}
