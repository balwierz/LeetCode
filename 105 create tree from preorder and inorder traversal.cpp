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
    void construct(int p0, int p1, int i0, int i1, vector<int>& p, vector<int>& i, TreeNode* n)
    { //p0, i0 point to current node, p1, i1 point to lastnode+1
        int thisVal = p[p0];
        n->val = thisVal;
        //cout << "p " << p0 << " " << p1 << " i " << i0 << " " << i1 << " val " << thisVal << endl;
        // find out how big the left subtree is:
        int newi1 = i0;
        int sizeLeft = 0;
        while(i[newi1] != thisVal)
        {
            sizeLeft ++;
            newi1++;
        }
        if(newi1 > i0)
        {
            n->left = new TreeNode;
            construct(p0+1, p0+1+sizeLeft, i0, newi1, p, i, n->left);
        }
        // find out how big the right subtree is:
        i0 = newi1 + 1;
        //p0 = i0;
        if(i0 < i1)
        {
            n->right = new TreeNode;
            construct(p0+1+sizeLeft, p1, i0, i1, p, i, n->right);
        }
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder)
    {
        TreeNode* root = new TreeNode;
        int n = preorder.size();
        construct(0, n, 0, n, preorder, inorder, root);
        return(root);
    }
};
