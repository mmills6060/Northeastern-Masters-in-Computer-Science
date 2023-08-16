// time complexity = O(n)
// space complexity - O(n)



class Solution {
public:
    void inOrder(TreeNode* root) {
        if (!root)
            return;
        inOrder(root->left);
        tree.push_back(root->val);
        inOrder(root->right);
    }
   
    bool isValidBST(TreeNode* root) {
        // base case
        if (!root)
            return true;
        
        // traverse the tree in order and store the results in tree
        inOrder(root);
        
        // if tree is not sorted, return false
        for (int i=1; i<tree.size(); i++)
            if (tree[i] <= tree[i-1])
                return false;
        
        // otherwise return true
        return true;
    }
private:
    vector<int> tree;
};