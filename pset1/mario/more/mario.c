#include <stdio.h>
#include <cs50.h>

int main(){
    int n;

    do
    {
        printf("Please specify the height of the pyramid: ");
        n=get_int();
    } while(n<0||n>23);

    for(int i=0;i<n;i++){
        for(int j=0;j<n-(i+1);j++){
            printf(" ");
        }
        for(int j=0;j<i+1;j++){
            printf("#");
        }
        printf("  ");
        for(int k=0;k<i+1;k++){
            printf("#");
        }

        printf("\n");
    }
}