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
class Solution {
public:
    bool find(TreeNode* root, int k, TreeNode* notThis)
    {
        while(true)
        {
            if(! root)
                return false;
            if(root->val == k && root != notThis)
                return true;
            if(k < root->val)
                root= root->left;
            else
                root = root->right;
        }
        return false;
    }
    bool dfs(TreeNode *node, int k, TreeNode *root)
    {
        if(!node)
            return false;
        if(find(root, k - node->val, node))
            return true;
        return dfs(node->left, k, root) || dfs(node->right, k, root);
    }
    bool findTarget(TreeNode* root, int k) 
    {
        return dfs(root, k, root);
    }
};
