#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[]){

	/*Validate input argument*/
	if(argc!=2){
		printf("only 1 argument is accepted");
		return 1;
	}

	string keyWord=argv[1];
	for(int i=0; i<strlen(keyWord); i++){
		if(!isalpha(keyWord[i])){
			printf("only alphabet is accepted");
			return 1;
		}
	}

	/*Main Program*/
	string plaintext = get_string("Input text: ");
	printf("plaintext: %s\n", plaintext);

	int counter=0;
	for (int i = 0; i < strlen(plaintext); ++i)
	{
		if(isalpha(plaintext[i])){
			int counterKey=counter%strlen(keyWord);
			int key=0;
			if(isupper(keyWord[counterKey])){
				key=keyWord[counterKey]-65;
			} else{
				key=keyWord[counterKey]-97;
			}
			if(isupper(plaintext[i])){
				// int key=(keyWord[counterKey]);
				plaintext[i]= 65+(plaintext[i]-65+key)%26;
				printf("plaintext[i] %c\n", plaintext[i]);
			} else{
				// int key=(keyWord[counterKey]);
				plaintext[i]= 97+(plaintext[i]-97+key)%26;
				printf("plaintext[i] %c\n", plaintext[i]);
			}
			counter++;
		}
	}

	printf("ciphertext: %s\n", plaintext);
}
