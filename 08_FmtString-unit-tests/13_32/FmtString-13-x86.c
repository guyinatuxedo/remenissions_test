#include <stdio.h>
#include <stdlib.h>

void main(void)
{
        char buf[80];

        printf("Tell me I was never good enough: %p\n", buf);

        fgets(buf, 83, stdin);

        printf(buf);

        exit(0);
}
