#include <stdio.h>
#include <stdlib.h>

void main(void)
{
        char buf[130];

        printf("Tell me I was never good enough: %p\n", buf);

        fgets(buf, sizeof(buf), stdin);

        printf(buf);

        exit(0);
}
