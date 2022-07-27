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
    TreeNode* flatten2(TreeNode *root)
    {
        TreeNode *tail = root;
        TreeNode *tmp = root->right;
        //cout << "at " << root->val << endl;
        if(root->left)
        {
            //cout << "left to " << root->left->val << endl;
            tail = flatten2(root->left);
            root->right = root->left;
            root->left = nullptr;
            tail->right = tmp;
        }
        if(tmp)
        {
            //cout << "right to " << tmp->val << endl;
            tail = flatten2(tmp);
        }
        return tail;
    }
    TreeNode *temp = nullptr;
public:
    void flatten(TreeNode* root)
    {
        if(root == nullptr)
            return;
        //flatten2(root);
        
        cout << "Flattening " << root->val << endl;
        flatten(root->right);
        flatten(root->left);
        
        root->right=temp;
        root->left=NULL;
        
        cout << "temp=" << root->val << endl;
        temp=root;
    }
};
