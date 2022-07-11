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
    vector<int> ret;
    int k=-1;
    void dfs(TreeNode* n, int lvl)
    {
        if(lvl > k)
        {
            ret[++k] = n->val;
        }
        if (n->right != nullptr)
            dfs(n->right, lvl+1);
        if (n->left != nullptr)
            dfs(n->left, lvl+1);
    }
public:
    vector<int> rightSideView(TreeNode* root) 
    {
        if(root == nullptr)
            return vector<int>(0);
        ret = vector<int>(100);
        dfs(root, 0);
        vector<int> ret2(k+1);
        for(int i=0; i<=k; i++)
            ret2[i] = ret[i];
        return ret2;
    }
};
