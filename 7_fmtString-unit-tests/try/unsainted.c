#include <stdio.h>
#include <stdlib.h>

void main(void)
{
	char hi[40];

	fgets(hi, sizeof(hi), stdin);
	printf("%s", hi);
}
