#include <stdio.h>
#include <stdlib.h>

void vuln(void)
{
        char buf[150];

        printf("Tell me I was never good enough: %p\n", buf);

        fgets(buf, sizeof(buf), stdin);

        printf(buf);
}

void main(void)
{
	vuln();
}
