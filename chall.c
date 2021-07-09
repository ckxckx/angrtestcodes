#include<stdio.h>
char aaa;
char bbb;

int main(int argc, char** argv){
    int ret = -99;
    aaa=argv[1][0];
    bbb = aaa+1;

    if(bbb=='b'){
        ret = 1;
        // if(argv[1][1]=='b'){
        //     ret=2;
        //     if(argv[1][2]=='c'){
        //         ret=3;
        //     }
        // }
    }


    return ret;

}