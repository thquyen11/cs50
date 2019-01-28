#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>


int main(int argc, string argv[]){
    if(argc<2||argc>2){
        printf("Only 1 argument allow\n");
        return 1;
    }

    int key = atoi(argv[1]);
    string plaintext;
    const int ascii_a=97;
    const int ascii_z=122;
    const int ascii_A=65;
    const int ascii_Z=90;

    plaintext = get_string("Input plain text: ");
    printf("plaintext: %s\n", plaintext);

    unsigned long len=strlen(plaintext);
    for(int i=0; i<len;i++){
        int ascii= (int) plaintext[i];
        int step=0;
        if(ascii>=ascii_A && ascii<=ascii_Z){
            step=(ascii+key-ascii_A)%26;
            ascii=ascii_A+step;
        } else if(ascii>=ascii_a && ascii<=ascii_z){
            step=(ascii+key-ascii_a)%26;
            ascii=ascii_a+step;
        }

        plaintext[i]=ascii;
    }

    printf("ciphertext: %s\n", plaintext);

}
