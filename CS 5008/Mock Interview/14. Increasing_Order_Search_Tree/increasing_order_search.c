  // time complexity = O(n)
  // space complexity = O(n)

    void inorder(TreeNode*& ans, TreeNode* root) {
        // Base case
        if (!root) return;
        // Visit the left child
        inorder(ans, root->left);
        // Visit the root
        ans->right = new TreeNode(root->val);
        ans = ans->right;
        // Visit the right child
        inorder(ans, root->right);
    }
    TreeNode* increasingBST(TreeNode* root) {
        // Create a temporary pointer to the answer
        TreeNode* temp;
        // Create an empty answer node
        TreeNode* ans = new TreeNode();
        // Set the temporary pointer to the answer node
        temp = ans;
        // Inorder traversal of the tree
        inorder(ans, root);
        // Return the answer node
        return temp->right;
    }