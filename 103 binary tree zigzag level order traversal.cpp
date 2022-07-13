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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) 
    {
        vector<deque<TreeNode*>> q(2);
        vector<vector<int>> ret;
        if(!root)
            return ret;
        int thisQueue = 0;
        q[thisQueue].push_back(root);
        while(! q[thisQueue].empty())
        {
            vector<int> row;
            while(! q[thisQueue].empty())
            {
                TreeNode* curr; 
                if(!thisQueue)   // left to right
                {
                    curr = q[thisQueue].front();
                    q[thisQueue].pop_front();
                    if(curr->left)
                        q[1-thisQueue].push_back(curr->left);
                    if(curr->right)
                        q[1-thisQueue].push_back(curr->right);
                }
                else
                {
                    curr = q[thisQueue].back();
                    q[thisQueue].pop_back();                    
                    if(curr->right)
                        q[1-thisQueue].push_front(curr->right);
                    if(curr->left)
                        q[1-thisQueue].push_front(curr->left);
                }
                
                row.push_back(curr->val);
            }
            ret.push_back(row);
            thisQueue = 1-thisQueue;  // swap
        }
        return ret;    
    }
};

