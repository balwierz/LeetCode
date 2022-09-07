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
    string tree2str(TreeNode* root)
    {
        string ret = to_string(root->val);
        if(root->right)
        {
            ret += "(";
            if(root->left)
                ret += tree2str(root->left);
            ret += ")(" + tree2str(root->right) + ")";
        }
        else if(root->left)
        {
            ret += "(" + tree2str(root->left) + ")";
        }
        return ret;
    }
};
