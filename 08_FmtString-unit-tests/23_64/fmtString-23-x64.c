#include <stdio.h>
#include <stdlib.h>

void pwned()
{
	system("/bin/sh");
}

void vuln(void)
{
        char buf[500];

        fgets(buf, sizeof(buf), stdin);

        printf(buf);

	fflush(stdin);
}

void main(void)
{
	int i;
	for (i = 0; i < 3; i++)
	{
		vuln();
	}
}
