#include <stdio.h>
#include <stdlib.h>

void main(void)
{
	int i;
	for (i = 0; i < 3; i++)
	{
		char buf[500];

	        fgets(buf, sizeof(buf), stdin);

	        printf(buf);
	}
}
