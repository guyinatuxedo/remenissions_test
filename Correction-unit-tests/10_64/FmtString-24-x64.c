#include <stdio.h>
#include <stdlib.h>

void main(void)
{
	char buf[100];
	int i;

	for (i = 0; i < 3; i++)
	{
		fgets(buf, sizeof(buf), stdin);

		printf(buf);
	}


}
