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
 *	Finds the index of where to insert to hash_set
 */
int find_index(int hash, int j) {
	return (hash + (j*j) + 23*j) % TABLE_SIZE;
}

/**
 *	Inserts a key into the hash_set
 */
int insert_key(hash_set* set, char* key) {
	int j = 0;
	int index, key_hash = hash(key);
	while(++j <= 19) {
		index = find_index(key_hash, j);
		if (set->keys[index] == NULL) {
			set->keys[index] = key;
			++set->num_keys;
			//printf("Inserted '%s' in index: %i\n", set->keys[index], index);
			break;
		}
	}
	return index;
}

/**
 *	Deletes a key from the hash_set
 */
int delete_key(hash_set* set, char* key) {
	printf("here\n");
	int index, key_hash = hash(key);
	for (int j = 1; j <= 19; ++j) {
		index = find_index(key_hash, j);
		if (strcmp(set->keys[index], key) == 0) {
			set->keys[index] = NULL;
			--set->num_keys;
			break;
		}
	}
	return index;
}

/**
 *	Prints the hash_set as per SPOJ specs
 */
void display_keys(hash_set* set) {
	int count = 0;
	for (int i = 0; i < TABLE_SIZE; ++i) {
		if (set->keys[i] != NULL) {
			++count;
		}
	}
	printf("%d\n", count);
	for (int i = 0; i < TABLE_SIZE; ++i) {
		if (set->keys[i] != NULL) {
			printf("%d:%s\n", i, set->keys[i]);
		}
	}
}


int main() {
	int num_sets, num_ops;
	//char cmd[4];
	//char key_val[MAX_KEY_SIZE+1];
	char input[MAX_KEY_SIZE+15];
	hash_set* set = new_set();
	// For each test case
	scanf("%d", &num_sets);

	for (int i = 0; i < num_sets; ++i) {
		// read in number of operations
		scanf("%d", &num_ops);
		// for each operation, do i
		for (int op = 0; op < num_ops; ++op) {
			//printf("op is: %d, num_op is: %d\n", op, num_ops);
			scanf("%s", input);
			if (*input == 'A') {
				insert_key(set, strdup(input+4));
			} else if (*input == 'D') {
				delete_key(set, strdup(input+4));
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















