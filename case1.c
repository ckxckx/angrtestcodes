int foo1(){

    int a=0;
    return a+1;
}

int foo2(){

    int a=0;
    return a+2;
}


int kk = 3;

int main(int argc, char** argv){

        if (kk>2){
            foo1();
        }
        else{
            foo2();
        }

}