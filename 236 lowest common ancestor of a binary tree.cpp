/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)
    {
        int nFound = 0;
        unordered_map<int, TreeNode*> parent;
        parent[root->val] = NULL;
        stack<TreeNode*> st;
        st.push(root);
        while(! st.empty())
        {
            TreeNode *t = st.top();
            st.pop();
            if(t == p || p == q)
            {
                if(++nFound == 2)
                    break;
            }
            if(t->left)
            {
                parent[t->left->val] = t;
                st.push(t->left);
            }
            if(t->right)
            {
                parent[t->right->val] = t;
                st.push(t->right);
            }
        }
        unordered_set<TreeNode*> anc;
        while(p)
        {
            anc.insert(p);
            p = parent[p->val];
        }
        while(q)
        {
            if(anc.count(q))
                return q;
            q = parent[q->val];
        }
        return root; // will never happen
    }
};
