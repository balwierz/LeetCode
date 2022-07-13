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
    vector<vector<int>> levelOrderBottom(TreeNode* root)
    {
        queue<TreeNode*> q;
        vector<vector<int>> ret;
        if(!root)
            return ret;
        q.push(root);
        while(!q.empty())
        {
            int n = q.size();
            vector<int> level;
            for(int i=0; i<n; i++)
            {
                TreeNode* n = q.front();
                q.pop();
                level.push_back(n->val);
                if(n->left)
                    q.push(n->left);
                if(n->right)
                    q.push(n->right);
            }
            ret.push_back(level);
        }
        reverse(ret.begin(), ret.end());
        return(ret);
    }
};
