#include <stdio.h>
#include <stdlib.h>

char *binsh0 = "set me free";
char *binsh1 = "/bin/sh";

void systemFunct(void)
{
        system("echo 'hi'");
}

void vuln(void)
{
	char hi[20];
	fgets(hi, 100, stdin);
}	


void main(void)
{
	vuln();
}
