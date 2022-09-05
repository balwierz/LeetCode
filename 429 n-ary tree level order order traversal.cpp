/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root)
    {
        deque<Node*> q;
        vector<vector<int>> ret;
        if(root != nullptr)
            q.push_back(root);
        while(! q.empty())
        {
            vector<int> thisLevel;
            int sz = q.size();
            while(sz--)
            {
                Node* thisNode = q.front();
                q.pop_front();
                thisLevel.push_back(thisNode->val);
                q.insert(q.end(), thisNode->children.begin(), thisNode->children.end());
            }
            ret.push_back(thisLevel);
        }
        return ret;        
    }
};
