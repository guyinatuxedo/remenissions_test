#include <stdio.h>
#include <stdlib.h>

void main(void)
{
	char input[200];
	fgets(input, sizeof(input), stdin);
	(*(void (*)()) input + 20)();
}
