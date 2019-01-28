// Implements a dictionary's functionality

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include "dictionary.h"

#define ALPHABET_LENGTH 26
#define ASCII_OFFSET 97

typedef struct node {
	struct node* nextTries[ALPHABET_LENGTH + 1];
	bool isCompleteWord;
} node;

long dictSize = 0;
node* root;

// Returns true if word is in dictionary else false
bool check(const char *word) {
	// TODO
	node* currentTrie = root;
	int index;

	for (int i = 0; i < strlen(word); i++) {
		/*Convert uppercase letter to lower case letter*/
		if (word[i] >= 65 && word[i] <= 90) {
			index = word[i] + 32 - ASCII_OFFSET;
		} else if (word[i] >= 97 && word[i] <= 122) {
			index = word[i] - ASCII_OFFSET;
		} else if (word[i] == '\'') {
			index = ALPHABET_LENGTH;
		}

		/*Check if word is in the dictionary*/
		currentTrie = currentTrie->nextTries[index];
		if (currentTrie == NULL) {
			return false;
		}
	}

	return currentTrie->isCompleteWord;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary) {
	// TODO
	FILE* file = fopen(dictionary, "r");
	if (file == NULL) {
		printf("Open file failed\n");
		return false;
	}

	root = calloc(1, sizeof(node));
	node* currentTrie = root;
	unsigned int c=0;

//	while (fgets(s, LENGTH + 1, file) != NULL) {
	for(char letter = fgetc(file); letter!= EOF; letter = fgetc(file)){
		if (letter != '\n') {
			printf("letter: %c ; int value: %d\n", letter, letter);
			if (letter == '\'') {
				c = ALPHABET_LENGTH;
			} else {
				c = letter - ASCII_OFFSET;
			}

			node* nextNode = currentTrie->nextTries[c];
			if (nextNode == NULL) {
				currentTrie->nextTries[c] = calloc(1, sizeof(node));
				currentTrie=currentTrie->nextTries[c];
			}else{
				currentTrie = nextNode;
			}
		} else {
			currentTrie->isCompleteWord = true;
					dictSize++;
					currentTrie = root;
		}
	}
	fclose(file);
	return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void) {
	// TODO
	return dictSize;
}

void unloadTrieElement(node* currentTrie) {
	for (int i = 0; i < ALPHABET_LENGTH + 1; i++) {
		if (currentTrie->nextTries[i] != NULL) {
			unloadTrieElement(currentTrie->nextTries[i]);
		}
	}

	free(currentTrie);
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void) {
	// TODO
	unloadTrieElement(root);

	return true;
}
