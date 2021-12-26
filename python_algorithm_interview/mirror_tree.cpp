#include <iostream>

using namespace std;

typedef struct Tree {
	int value;
	Tree* left_child;
	Tree* right_child;
	Tree(int value): value(value), left_child(nullptr), right_child(nullptr) {}
	
}Tree;

Tree* mirror_tree(Tree* root) {
	if (root) {
		mirror_tree(root->left_child);
		mirror_tree(root->right_child);

		Tree* tmp;
		tmp = root->left_child;
		root->left_child = root->right_child;
		root->right_child = tmp;
	}
	return root;
}


int main()
{
	Tree* root = new Tree(1);
	root->value = 1;
	root->left_child = new Tree(2);
	root->right_child = new Tree(3);

	Tree* left_child = root->left_child;
	left_child->left_child = new Tree(4);
	left_child->right_child = new Tree(5);

	mirror_tree(root);
	
	cout << endl;
}
