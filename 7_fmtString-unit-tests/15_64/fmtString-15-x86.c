#include <stdio.h>
#include <stdlib.h>

void notPwned0(void)
{
	system("echo 'so far away'");
}

void pwned(void)
{
	system("/bin/sh");
}

void notpwned1(void)
{
	system("echo 'tell my baby girl it's alright'");
}

void main(void)
{
	char buf[150];

	printf("Total Nightmare: %p\n", main);

	fflush(stdin);

	fgets(buf, sizeof(buf), stdin);

	printf(buf);

	fflush(stdin);
}