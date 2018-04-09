/**
 *  Taylor He, Jacob Manzelmann, Thomas Osterman
 *  CS370 Assignment 3: Trie
 *  I pledge my honor that I have abided by the Stevens Honor System.
 *  -Taylor, Jacob, Thomas
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ALPHABET_LENGTH    26
#define OPERATION_BUF_SIZE  5
#define NAME_BUF_SIZE      22
#define LOWER_ASCII_OFFSET 97

// node struct for trie
typedef struct node {
    int num_children;
    struct node* children[ALPHABET_LENGTH];
} trie_node;

/**
 *  Mallocs a new node with size int + 26*node
 *  Initializes the fields of nodes with 0 and NULL
 */
struct node* new_node() {
	struct node* n_node = malloc(sizeof(int) + sizeof(struct node*) * ALPHABET_LENGTH);
	n_node->num_children = 0;
	for (int i =0; i< ALPHABET_LENGTH - 1; ++i) {
		n_node->children[i] = NULL;
	}
	return n_node;
}

/** 
 *  Recursively adds each char of a given char* to the trie
 */
void add(struct node* trie, char* name) {
	trie->num_children += 1;
  if (*name == '\0') return;
	if (trie->children[*(name) - LOWER_ASCII_OFFSET] == NULL) {
		trie->children[(*name) - LOWER_ASCII_OFFSET] = new_node();
		add(trie->children[(*name) - LOWER_ASCII_OFFSET], name+1);
	} else {
    add(trie->children[(*name) - LOWER_ASCII_OFFSET], name+1);
  }
}

/**
 *  Returns the number of items in the trie that start with
 *  the given char*
 */
int find(struct node* trie, char* partial){
	if (trie == NULL) {
		return 0;
	}
	if (*partial != '\0') {
		return find(trie->children[(*partial) - LOWER_ASCII_OFFSET], partial+1);
	}
	return trie->num_children;
}

/**
 *  Frees the trie upon completion
 */
void free_trie(struct node* trie){
  if (trie == NULL){
    return;
  }
  for(int i = 0; i < ALPHABET_LENGTH; i++){
    free_trie(trie->children[i]);
  }
  free(trie);
}

// Asks for user input to add and find contacts
int main() {
	struct node* trie = new_node();

  int num_cases;  // Number of commands
  char name[NAME_BUF_SIZE];  // Name of contact to add
  char buffer[OPERATION_BUF_SIZE+NAME_BUF_SIZE+1]; // Input buffer

  // Get the number of cases
  scanf("%d\n", &num_cases);

  for(int i = 0; i < num_cases; i++){
    // First get the input command
    fgets(buffer, OPERATION_BUF_SIZE+NAME_BUF_SIZE+1, stdin);
    // Don't read in the newline
    if (buffer[strlen(buffer)-1] == '\n'){
      buffer[strlen(buffer)-1] = 0;
    } 
    // Check first letter
    if(buffer[0] == 'a'){
      add(trie, buffer+OPERATION_BUF_SIZE-1);
    } else if(buffer[0] == 'f') {
      printf("%d\n", find(trie, buffer+OPERATION_BUF_SIZE));
    } else {
      printf("Unrecognized command\n");
    }
    // clears the variables.
    memset(buffer, '\0', OPERATION_BUF_SIZE+NAME_BUF_SIZE+1);
    memset(name, '\0', NAME_BUF_SIZE);
  }

  free_trie(trie);
}
