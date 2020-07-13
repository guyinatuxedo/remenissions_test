#include <stdio.h>
#include <stdlib.h>


void pwned(void)
{
        system("/bin/sh");
}

void vuln(void)
{
        char buf[37];

        printf("Tell me I was never good enough: %p\n", buf);

        fgets(buf, sizeof(buf), stdin);

        printf(buf);
}

void main(void)
{
	vuln();
}
