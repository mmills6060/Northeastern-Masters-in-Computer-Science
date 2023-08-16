// time complexity = O(n)
// space complexity - O(n)


int maxDepth(TreeNode* root) {
        // check if root is null, if so, return 0
        if(!root) return 0;
        // get the max depth of the left subtree
        int maxLeft = maxDepth(root->left);
        // get the max depth of the right subtree
        int maxRight = maxDepth(root->right);
        // return the max depth between left and right subtree + 1 (to account for the current node)
        return max(maxLeft, maxRight)+1;
    }