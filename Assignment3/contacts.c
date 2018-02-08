#include <stdio.h>
#include <stdlib.h>
#define ALPHABET_LENGTH    26
#define OPERATION_BUF_SIZE  5
#define NAME_BUF_SIZE      22

typedef struct node {
    int num_children;
    struct node* children[ALPHABET_LENGTH];
} trie_node;

struct node* new_node() {
	struct node* n_node = malloc(sizeof(int) + sizeof(struct node*) * 26);
	n_node->num_children = 0;
	for (int i =0; i< ALPHABET_LENGTH - 1; ++i) {
		n_node->children[i] = NULL;
	}
	return n_node;
}

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

int find(struct node* trie, char* partial) {
	if (trie == NULL) {
		return 0;
	}
	if (*partial != '\0') {
		return find(trie->children[(*partial) - 97], partial+1);
	}
	return trie->num_children;
}

int main() {
	struct node* trie = new_node();

	int num_cases = scanf()
}