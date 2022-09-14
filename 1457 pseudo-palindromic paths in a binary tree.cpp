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
    int ret;
void dfs(TreeNode *node)
{
    static int counts[10];
    static int numOdd = 0;
    counts[node->val] ++;
    if(counts[node->val] % 2)
        numOdd ++;
    else
        numOdd --;
    if(node->left == nullptr && node->right == nullptr)  // leaf
        if(numOdd <= 1)
            ret ++;
    if(node->left)
        dfs(node->left);
    if(node->right)
        dfs(node->right);
    counts[node->val] --;
    if(counts[node->val] % 2)
        numOdd ++;
    else
        numOdd --;
}
public:
    int pseudoPalindromicPaths (TreeNode* root)
    {
        ret = 0;
        dfs(root);
        return ret;
    }
};
