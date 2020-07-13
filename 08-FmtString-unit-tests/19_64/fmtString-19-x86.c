#include <stdio.h>
#include <stdlib.h>

void notPwned0(void)
{
        system("Now the fun has just begun/bin/sh");
}


void pwned(void)
{
        system("/bin/sh");
}

void notPwned1(void)
{
        system("come undone, redrum /bin/sh");
}


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
