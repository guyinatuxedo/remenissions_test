#include <stdio.h>
#include <stdlib.h>

void win(void)
{
	system("/bin/sh");
}

void vuln(void)
{
	char hi[20];
	fgets(hi, 50, stdin);

}

int main(void)
{
	vuln();
}
