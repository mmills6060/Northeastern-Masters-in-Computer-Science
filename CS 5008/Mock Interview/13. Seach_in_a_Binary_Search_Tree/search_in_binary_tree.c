/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */


// time complexity = O(n)
// space complexity = O(n)
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        // If the root is NULL, return NULL
        if(root == NULL) return NULL;
        // If the root's value is equal to val, return the root
        if(root->val == val) return root;

        // If val is less than the root's value, search the left subtree
        if(val < root->val) root = searchBST(root->left, val);
        // If val is greater than the root's value, search the right subtree
        else root = searchBST(root->right, val);

        // Return the root
        return root;
    }
};