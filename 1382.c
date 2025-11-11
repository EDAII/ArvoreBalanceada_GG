#include <stdlib.h>

struct TreeNode* createNode(int val) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->val = val;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

int countNodes(struct TreeNode* root) {
    if (root == NULL) {
        return 0;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
}

void inorderValues(struct TreeNode* root, int* arr, int* index) {
    if (root == NULL) {
        return;
    }
    inorderValues(root->left, arr, index);
    arr[(*index)++] = root->val;
    inorderValues(root->right, arr, index);
}

struct TreeNode* buildBalanced(int* arr, int start, int end) {
    if (start > end) {
        return NULL;
    }

    int mid = start + (end - start) / 2;
    struct TreeNode* root = createNode(arr[mid]);

    root->left = buildBalanced(arr, start, mid - 1);
    root->right = buildBalanced(arr, mid + 1, end);

    return root;
}


struct TreeNode* balanceBST(struct TreeNode* root) {
    if (root == NULL) {
        return NULL;
    }

    int n = countNodes(root);

    int* values = (int*)malloc(n * sizeof(int));
    int index = 0;
    inorderValues(root, values, &index);

    struct TreeNode* newRoot = buildBalanced(values, 0, n - 1);

    free(values);

    return newRoot;
}