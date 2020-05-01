#include <stdio.h>
#include <stdlib.h>

void win(void)
{
	system("/bin/sh");
}

void vuln(void)
{
	char hi[20];
	printf("The sin, and the sentece: %p\n", vuln);
	fgets(hi, 50, stdin);

}

int main(void)
{
	vuln();
}
