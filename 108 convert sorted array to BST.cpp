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
    void helper(vector<int> &nums, TreeNode *root, int i, int j)
    {
        int mid = (i + j) / 2;
        root->val = nums[mid];
        if(mid>i)
        {
            root->left = new TreeNode;
            helper(nums, root->left, i, mid);
        }
        if(mid+1<j)
        {
            root->right = new TreeNode;
            helper(nums, root->right, mid+1, j);
        }
    }
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode *root = new TreeNode;
        helper(nums, root, 0, nums.size());
        return root;
    }
};
