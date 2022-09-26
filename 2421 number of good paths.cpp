class UF
{
    vector<int> parent;
public:
    UF(int size)
    {
        parent.resize(size);
        for(int i=1; i<size; i++)
            parent[i] = i;
    }
    int find(int x)
    {
        if(parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
    void merge(int a, int b)
    {
        int ra = find(a);
        int rb = find(b);
        if( ra == rb)
            return;
        parent[ra] = rb;
    }
};
class Solution {
public:
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) 
    {
        int n = vals.size();
        UF uf(n);
        vector<vector<int>> neigh(n);
        for(vector<int> &e : edges)
        {
            neigh[e[0]].push_back(e[1]);
            neigh[e[1]].push_back(e[0]);
        }
        vector<pair<int, int>> val_idx;
        for(int i=0; i<n; i++)
        {
            val_idx.push_back({vals[i], i});
        }
        sort(val_idx.begin(), val_idx.end());
        int lastVal = val_idx[0].first;
        int i = 0;
        int ret = n;
        while(true)
        {
            vector<int> newIndices;
            while(i < n && val_idx[i].first == lastVal)
            {
                int thisNode = val_idx[i].second;
                newIndices.push_back(thisNode);
                for(int other : neigh[thisNode])
                {
                    if(vals[other] <= lastVal)
                        uf.merge(thisNode, other);
                }
                i++;
            }
            if(newIndices.size() > 1)
            {
                unordered_map<int, int> root2count;
                for(int index : newIndices)
                    root2count[uf.find(index)] ++;
                
                for(auto [root, count] : root2count)
                    ret += count * (count - 1) / 2;
            }
            if(i == n)
                break;
            lastVal = val_idx[i].first;
        }
        return ret;
    }
};
