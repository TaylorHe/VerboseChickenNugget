#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ALPHABET_LENGTH    26
#define OPERATION_BUF_SIZE  5
#define NAME_BUF_SIZE      22

//node struct for trie
typedef struct node {
    int num_children;
    struct node* children[ALPHABET_LENGTH];
} trie_node;

//function to malloc a new node with base parameters
struct node* new_node() {
	struct node* n_node = malloc(sizeof(int) + sizeof(struct node*) * 26);
	n_node->num_children = 0;
	for (int i =0; i< ALPHABET_LENGTH - 1; ++i) {
		n_node->children[i] = NULL;
	}
	return n_node;
}

//function to add a contact to the trie
void add(struct node* trie, char* name) {
	trie->num_children += 1;
	if (*name != '\0') {
		if (trie->children[*(name) - 97] == NULL) {
			trie->children[(*name) - 97] = new_node();
			add(trie->children[(*name) - 97], name+1);
			return;
		}
		add(trie->children[(*name) - 97], name+1);
		return;
	}
	return;
}

//function that returns the number of contacts that start with "partial"
int find(struct node* trie, char* partial){
	if (trie == NULL) {
		return 0;
	}
	if (*partial != '\0') {
		return find(trie->children[(*partial) - 97], partial+1);
	}
	return trie->num_children;
}

//function to free the memory upon completion
void free_trie(struct node* trie){
  if (trie == NULL){
    return;
  }
  for(int i = 0; i < ALPHABET_LENGTH; i++){
    free_trie(trie->children[i]);
  }
  free(trie);
}

//main method asks for user input to add and find contacts
int main() {
	struct node* trie = new_node();
  /*add(trie, "hello");
  add(trie, "he");
  printf("%d\n", find(trie, "h"));*/
  int num_cases;
  char name2[NAME_BUF_SIZE];
  char* name = name2;
  char buffer[OPERATION_BUF_SIZE+NAME_BUF_SIZE];
  scanf("%d\n", &num_cases);
  for(int i = 0; i < num_cases; i++){
    fgets(buffer, OPERATION_BUF_SIZE+NAME_BUF_SIZE, stdin);
    //printf("%s\n", buffer);
    if(buffer[3] == ' '){
      //memcpy(name, buffer+4, strlen(buffer+4)+1);
      //printf("%s\n", name);
      add(trie, buffer+4);
    }
    else{
      //memcpy(name, buffer+5, strlen(buffer+5)+1);
      //printf("%s\n", name);
      printf("%d\n", find(trie, "h"));
      printf("%d\n", find(trie, buffer+5));
    }
    memset(buffer, '\0', OPERATION_BUF_SIZE+NAME_BUF_SIZE);
    memset(name, '\0', NAME_BUF_SIZE);
  }

  free_trie(trie);
}
