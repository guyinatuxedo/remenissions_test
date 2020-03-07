#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

void main(void)
{
	void *inp;
	inp = mmap(0, 200, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_ANON | MAP_PRIVATE, 0, 0);
	fgets(inp, 200, stdin);
	(*(void (*)()) inp + 37)();
}
