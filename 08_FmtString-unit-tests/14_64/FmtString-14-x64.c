#include <stdio.h>
#include <stdlib.h>

void notPwned0(void)
{
	system("echo 'so far away'");
}

void pwned(void)
{
	system("echo 'I think I think too much'");
}

void notpwned1(void)
{
	system("/bin/sh");
}

void main(void)
{
	char buf[150];

	fflush(stdin);

	fgets(buf, sizeof(buf), stdin);

	printf(buf);

	fflush(stdin);
}
