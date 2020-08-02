#include <stdio.h>
#include <stdlib.h>

void falseWin0(void)
{
	system("trashed and scattered");
}

void win(void)
{
	system("/bin/sh");
}

void falseWin1(void)
{
	system("people = shit");
}

void falseWin2(char inp)
{
	system(inp);
}

void vuln(void)
{
	char vulnBuf[20];

	printf("Is it a sin, to miss the hell: %p\n", vuln);
	fgets(vulnBuf, 100, stdin);

}

void main(void)
{
	vuln();
}
