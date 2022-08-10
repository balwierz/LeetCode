class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted)
    {
        //unordered_set<int> restr(restricted.begin(), restricted.end());
        vector<bool> restr(n, false);
        for(int i:restricted)
            restr[i] = true;
        vector<forward_list<int>> neigh(n);
        
        for(vector<int> &edge : edges)
        {
            //if(!restr.count(edge[0]) && !restr.count(edge[1]))
            if(!restr[edge[0]] && !restr[edge[1]])
            {
                neigh[edge[0]].push_front(edge[1]);
                neigh[edge[1]].push_front(edge[0]);
            }
        }
        int ret = 0;
        stack<int> st;
        st.push(0);
        bool *visited = new bool[n];
        memset(visited, false, sizeof(bool)*n);
        while(! st.empty())
        {
            int node = st.top();
            st.pop();
            ret++;
            visited[node] = true;
            for(int n:neigh[node])
                if(!visited[n])
                    st.push(n);
        }
        return ret;
    }
};
