#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void pwned()
{
	system("/bin/sh");
}


void main(void)
{
	char buf[500];
	int i;

	for (i = 0; i < 3; i++)
	{

        	memset(buf, 0x0, 300);

        	fgets(buf, sizeof(buf), stdin);

        	strncpy(buf + 300, (char *)main, 10);

        	printf(buf);
        
        	fflush(stdin);
	}
}
