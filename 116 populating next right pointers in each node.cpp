/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution 
{
    struct elem
    {
        Node *n;
        int depth;
        elem(Node *m, const int &w) : n(m), depth(w) {}
    };
public:
    Node* connect(Node* root) 
    {
        queue<elem> q;
        if(! root)
            return NULL;
        q.emplace(root, 0);
        int lastDepth = -1;
        Node *lastNode = NULL;
        while(! q.empty())
        {
            elem e = q.front();
            q.pop();
            if(e.depth > lastDepth)
            {
                // rightmost element
                e.n->next = NULL;
                lastDepth = e.depth;
            }
            else
            {
                e.n->next = lastNode;
            }
            lastNode = e.n;
            if(e.n->right)
            {
                q.emplace(e.n->right, e.depth+1);
                q.emplace(e.n->left , e.depth+1);
            }
        }
        return(root);
    }
};
