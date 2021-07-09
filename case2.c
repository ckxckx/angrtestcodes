
int kk = 1;

int kkk= 8;

int foo1(){

    int a=0;

    if (kkk<9){
        a+=1;
    }

    return a+1;
}

int foo2(){
    int a=0;

    if (kkk<9){
        a+=1;
    }

    return a+2;
}



int main(int argc, char** argv){

        if (kk>2){
            foo1();
        }
        else{
            foo2();
        }

}