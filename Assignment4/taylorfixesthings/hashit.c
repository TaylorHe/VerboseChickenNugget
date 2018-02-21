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

hash_set* new_set() {
	hash_set *ns = malloc(sizeof(hash_set));
	ns->num_keys = 0;
	for(int i = 0; i < TABLE_SIZE; i++) {
		ns->keys[i] = (char*)calloc(sizeof(char), MAX_KEY_SIZE+5);
	}
  return ns;
}

/**
 *	Sets the set's keys to NULL and num_keys to 0
 */
void clear_table(hash_set* set) {
	for (int i = 0; i < TABLE_SIZE; ++i) {
		set->keys[i] = NULL;
		free(set->keys[i]);
	}
	set->num_keys = 0;
	free(set);
}

/**
 *	Hashes the char* according to SPOJ's specs
 */
int hash(char* key) {
	int len = strlen(key);
	long hash = 0;
	for (int i = 0; i < len; ++i) {
		hash += *(key+i) * (i+1);
	}
	return (hash * 19) % TABLE_SIZE;
}
/**
 *	Finds the index of where to insert to hash_set
 */
int find_index(int hash, int j) {
	return (hash + (j*j) + (23*j)) % TABLE_SIZE;
}

/**
 *	Finds a key in the hash_set. Returns true if exists, else false
 */
int find_key(hash_set* set, char* key) {
	int key_hash = hash(key);
	int index;
	// We can start at 0 because index doesn't change for j=0!
	for (int j = 0; j <= 19; ++j) {
		index = find_index(key_hash, j);
		if (set->keys[j] == NULL) {
			return 0;
		}
		if (strcmp(set->keys[index], key) == 0) {
			return 1;
		}
	}
	return 0;
}


/**
 *	Inserts a key into the hash_set
 *  Uses open addressing to resolve 
 */
int insert_key(hash_set* set, char* key) {
	int key_hash = hash(key);
	// If we can find it in the hash_set, then we can't add it.
	if (find_key(set, key) == 1) {
		return key_hash;
	}
	
	int index;
	for (int j = 0; j <= 19; ++j) {
		index = find_index(key_hash, j);
		if (strcmp(set->keys[index], "") == 0) {
			strcpy(set->keys[index], key);
			(set->num_keys)++;
			break;
		}
		// if (strcmp(set->keys[index], key) == 0) {
		// 	break;
		// }
	}
	return index;
}

/**
 *	Deletes a key from the hash_set
 */
int delete_key(hash_set* set, char* key) {
	int key_hash = hash(key);
	// if (set->keys[key_hash] != NULL){
	// 	if (strcmp(set->keys[key_hash], key) == 0) {
	// 		set->keys[key_hash] = NULL;
	// 		--set->num_keys;
	// 		return key_hash;
	// 	}	
	// }
	if (find_key(set, key) == 0) {
		return -1;
	} 
	int index;
	for (int j = 0; j <= 19; ++j) {
		index = find_index(key_hash, j);
		if (strcmp(set->keys[index], key) == 0) {
			strcpy(set->keys[index],"");
			(set->num_keys)--;
			break;
		}
	}
	return 1;
}

/**
 *	Prints the hash_set as per SPOJ specs
 */
void display_keys(hash_set* set) {
	printf("%d\n", set->num_keys);
	for (int i = 0; i < TABLE_SIZE; ++i) {
		// Display all that are not empty string
		if (strcmp(set->keys[i], "") != 0) {
			printf("%d:%s\n", i, set->keys[i]);
		}
	}
}


int main() {
	int num_sets;
		
	scanf("%d", &num_sets);
	// For each test case
	while (num_sets--) {
		//hash_set set = new_set();
		hash_set* set = new_set();
		
		// read in number of operations
		int num_ops;
		scanf("%d", &num_ops);

		char input[MAX_KEY_SIZE+5];
		// for each operation, do i
		for (int op = 0; op < num_ops; ++op) {
			//printf("op is: %d, num_op is: %d\n", op, num_ops);
			
			scanf("%s", input);
			// printf("in: '%s'\n", input+4);
			
			if (input[0] == 'A') {
				insert_key(set, input+4);
			} else {
				delete_key(set, input+4);
			}
		}

		// Display at the end of each test case
		display_keys(set);
		clear_table(set);
	}
	
	return 0;
}















