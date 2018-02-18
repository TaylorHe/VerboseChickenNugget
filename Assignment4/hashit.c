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
#define MAX_KEY_SIZE 15

/**
 *	typedef of a hashset
 */
typedef struct {
    char* keys[TABLE_SIZE];
    int num_keys;
} hash_set;

/**
 *	hash_set constructor
 */
hash_set* new_set() {
	hash_set* n_set = malloc(sizeof(char) * TABLE_SIZE * MAX_KEY_SIZE + sizeof(int));
	n_set->num_keys = 0;
	for (int i = 0; i < TABLE_SIZE; ++i) {
		n_set->keys[i] = NULL;
	}
	return n_set;
}

/**
 *	Sets the set's keys to NULL and num_keys to 0
 */
void clear_table(hash_set* set) {
	for (int i = 0; i < TABLE_SIZE; ++i) {
		set->keys[i] = NULL;
	}
	set->num_keys = 0;
}

/**
 *	Hashes the char* according to SPOJ's specs
 */
int hash(char* key) {
	int len = strlen(key);
	int hash = 0;
	for (int i = 0; i < len; ++i) {
		hash += *(key+i) * (i+1);
	}
	return (hash * 19) % TABLE_SIZE;
}

/**
 *	Inserts a key into the hash_set
 */
int insert_key(hash_set* set, char* key) {
	return 0;
}

/**
 *	Deletes a key from the hash_set
 */
int delete_key(hash_set* set, char* key) {
	return 0;
}

/**
 *	Prints the hash_set as per SPOJ specs
 */
void display_keys(hash_set* set) {
	int i = 0;
	for (i = 0; i < TABLE_SIZE-1; ++i) {
		if (set->keys[i] != NULL) {
			printf("%d:%s\n", i, set->keys[i]);
		}
	}
	// Don't print a newline at the end
	if (set->keys[i] != NULL) {
		printf("%d:%s", i, set->keys[i]);
	}
}


int main() {
	int num_sets, num_ops;
	char cmd[3], key_val[MAX_KEY_SIZE];
	scanf("%d\n", num_sets);
	hash_set* set = new_set();
	// For each test case
	for (int i = 0; i < num_sets; ++i) {
		// read in number of operations
		scanf("%d\n", num_ops);
		// for each operation, do it
		for (int op = 0; op < num_ops; ++op) {
			scanf("%s:%s", cmd, key_val);
			if (cmd == "ADD") {
				insert_key(key_val);
			} else if (cmd == "DEL") {
				delete_key(key_val);
			}
		}
		// Display at the end of each test case
		display_keys(set);
		// Clear the set for reuse
		clear_table(set);
	}
	free(set);
	return 0;
}















