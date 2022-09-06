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
    bool hasOne(TreeNode* p)
    {
        bool ret = false;
        if(p->left)
        {
            bool l=hasOne(p->left);
            if(l)
                ret = true;
            else
                p->left = nullptr;
        }
        if(p->right)
        {
            bool r = hasOne(p->right);
            if(r)
                ret = true;
            else
                p->right= nullptr;
        }
        return(ret || p->val);
    }
    TreeNode* pruneTree(TreeNode* root)
    {
        if(hasOne(root))
            return root;
        else
            return nullptr;
    }
};
