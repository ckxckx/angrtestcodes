#include<stdio.h>


// char mem[0x20];
char mem[0x20]="hellow!";



void hexdump(char *buf, int len)
{
    int i = 0;

    printf("\n----------------------hexdump------------------------\n");
    for(i = 0; i < len; i++) {
        printf("%02x ", buf[i]);
        if( (i+1) % 16 == 0) {
            printf("\n");
        }
    }

    if(i%16 != 0) {
        printf("\n");
    }

    printf("---------------------hexdump-------------------------\n\n");
}

int main()
{
    
    hexdump(mem,0x20);
    // printf("%x")
}