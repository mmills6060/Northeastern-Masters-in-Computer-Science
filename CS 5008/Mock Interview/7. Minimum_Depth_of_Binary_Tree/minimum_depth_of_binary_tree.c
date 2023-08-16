// time complexity = O(n)
// space complexity - O(n)


int minDepth(struct TreeNode* root){
    // 1. check if root is null
    if(root == NULL)
        return 0;
    else {
        // 2. calculate left depth
        int leftDepth = minDepth(root->left);
        // 3. calculate right depth
        int rightDepth = minDepth(root->right);
        // 4. compare left and right depth
        if(leftDepth > rightDepth)
            // 5. return the smaller depth + 1
            return rightDepth + 1;
        else
            return leftDepth + 1;
    }
}