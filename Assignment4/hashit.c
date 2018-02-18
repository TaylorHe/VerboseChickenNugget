/**
 *  Taylor He, Jacob Manzelmann, Thomas Osterman
 *  CS370 Assignment 3: Trie
 *  I pledge my honor that I have abided by the Stevens Honor System.
 *  -Taylor, Jacob, Thomas
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TABLE_SIZE 101

typedef struct {
    char* keys[TABLE_SIZE];
    int num_keys;
} hash_set;

hash_set* new_set() {
	hash_set* n_set = malloc(sizeof(char) * TABLE_SIZE + sizeof(int));
	n_set->num_keys = 0;
	for (int i =0; i< TABLE_SIZE - 1; ++i) {
		n_set->keys[i] = NULL;
	}
	return n_set;
}

void clear_table(hash_set* set) {
	for (int i=0; i<TABLE_SIZE; ++i) {
		set->keys[i] = NULL;
	}
	set->num_keys = 0;
}

int hash(char* key) {
	int len = strlen(key);
	int hash = 0;
	for (int i=0; i<len; ++i) {
		hash += *(key+i) * (i+1);
	}
	return (hash * 19) % TABLE_SIZE;
}

int insert_key(hash_set* set, char* key) {
	return 0;
}

int delete_key(hash_set* set, char* key) {
	return 0;
}

void display_keys(hash_set* set) {
	for (int i=0; i<TABLE_SIZE; ++i) {
		if (set->keys[i] != NULL) {
			printf("%d:%s\n", i, set->keys[i]);
		}
	}
}

int main() {
	return 0;
}