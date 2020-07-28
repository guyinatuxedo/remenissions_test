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
	char vuln[20];

	fgets(vuln, 100, stdin);

}

void main(void)
{
	vuln();
}
