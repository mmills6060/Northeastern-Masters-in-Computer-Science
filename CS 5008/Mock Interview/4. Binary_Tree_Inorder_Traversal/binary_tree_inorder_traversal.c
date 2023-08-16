// time complexity = O(n)
// space complexity - O(n)

void traverse(struct TreeNode* root, int* arr, int* returnSize){
    if(root->left)
        traverse(root->left,arr,returnSize);  //traverse left subtree
    arr[(*returnSize)++]=root->val;  //add current node
    if(root->right)
        traverse(root->right,arr,returnSize); //traverse right subtree
}

int* inorderTraversal(struct TreeNode* root, int* returnSize){
    int*arr=malloc(100*sizeof(int));
    *returnSize=0;
    if(root)
        traverse(root,arr,returnSize); //start traversal
    arr=realloc(arr,(*returnSize)*sizeof(int));
    return arr;
}