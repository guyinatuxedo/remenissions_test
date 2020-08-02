#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void win(void)
{
	FILE *fp;
	char flag[50];

	fp = fopen("flag.txt", "r");

	fgets(flag, sizeof(flag), fp);

	printf("flag: %s\n", flag);
}

void vuln(char *inp)
{
	char buf[10];
	strcpy(buf, inp);
}

void main(int argc, char **argv)
{
	vuln(argv[1]);
}
