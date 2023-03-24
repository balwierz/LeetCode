class Solution {
public:
    int ret;
    vector<vector<pair<int, bool>>> adj;
    Solution()
    {
        ret = 0;
    }
    void dfs(int node, int parent)
    {
        for(pair<int, bool> &neigh : adj[node])
        {
            if(neigh.first != parent)
            {   
                ret += neigh.second;
                dfs(neigh.first, node);
            }
        }
    }
    int minReorder(int n, vector<vector<int>>& connections) 
    {
        adj.resize(n);
        for(vector<int> &conn : connections)
        {
            adj[conn[0]].emplace_back(conn[1], true);
            adj[conn[1]].emplace_back(conn[0], false);
        }
        dfs(0, -1);
        return ret;
    }
};
