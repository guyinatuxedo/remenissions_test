#include <stdio.h>
#include <stdint.h>

void print_flag(){
    printf("Thank you! you can have your flag: ");
    FILE* f = fopen("flag.txt", "r");
    if(!f) {
        printf("flag not found\n");
        return;
    }
    char buf[29];
    fgets(buf, 29, f);
    printf("%s\n", buf);
    fclose(f);
}

int main(int argc, char** argv){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    uint8_t buffer[264];
    *(uint32_t*)&buffer[260] = 0xdeadbeef;
    printf("Hello! I am x86 vulnerable programm and have and inner buffer size of 256 bites\n"); 
    printf("Can you lead me to segmentation fault please?\n");
    fgets(buffer, 264, stdin);
    if(*(uint32_t*)&buffer[260] != 0xdeadbeef){
        print_flag();
    }else
        printf("Hit me harder!\n");
	return 0;
}
