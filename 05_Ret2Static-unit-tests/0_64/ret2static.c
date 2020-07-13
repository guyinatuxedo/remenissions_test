#include <stdio.h>
#include <stdlib.h>


void vuln(void)
{
	char buf[0x50];
	gets(buf);
}

void main(void)
{
	vuln();
}
