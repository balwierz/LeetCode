class Solution
{
    TreeNode *root;
    int depth;
    bool check(int val)  // val is binary representation of a path. fist 1 is to go to root.
    {
        TreeNode *p = root;
        for(int h=depth-1; h>=0; h--)
        {
            bool side = val & (1 << h);
            if(side)
                p = p->right;
            else
                p = p->left;
        }
        return p;  // if it is not null
    }
public:
    int countNodes(TreeNode* root)
    {
        if(!root)
            return 0;
        this->root = root;
        // get the depth:
        int h=0;
        TreeNode *p = root;
        while(p->left)
        {
            h++;
            p = p->left;
        }
        this->depth = h;
        cout << h;
        // the number of nodes to check: 2^h (1) -- 2^(h+1)-1 (2^h)
        int left = (1 << h); // for sure true
        int right = (1 << (h+1)); // for sure false
        while(left + 1 != right)
        {
            int mid = (left + right) / 2;
            if(check(mid))
                left = mid;
            else
                right = mid;
        }
        return left;
    }
};
