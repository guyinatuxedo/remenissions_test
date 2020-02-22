#include <stdio.h>
#include <stdlib.h>

void win(void)
{
        system("/bin/sh");
}

int main(void)
{
        char hi[20];
        printf("Pie Infoleak:%p\n", hi);
        gets(hi);
}    