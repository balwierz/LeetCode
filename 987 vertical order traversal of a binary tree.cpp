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
    map<int, map<int, multiset<int>>> tab;
    void dfs(TreeNode *node, int row, int col)
    {
        tab[col][row/2].insert(node->val);
        if(node->left)
            dfs(node->left, row+1, col-1);
        if(node->right)
            dfs(node->right, row+1, col+1);
    }
    vector<vector<int>> verticalTraversal(TreeNode* root)
    {
        dfs(root, 0, 0);
        vector<vector<int>> ret;
        for(auto colI = tab.begin(); colI!=tab.end(); colI++)
        {
            vector<int> colV ;
            for(auto rowI=colI->second.begin(); rowI!=colI->second.end(); rowI++)
            {
                for(auto elI=rowI->second.begin(); elI!=rowI->second.end(); elI++)
                    colV.push_back(*elI);
            }
            ret.push_back(colV);
        }
        return ret;
    }
}; 
