class Solution {
    unordered_map<int, int> row2root, col2root;
    vector<int> parent;
    int root(int e)
    {
        while(parent[e] != parent[parent[e]])
            parent[e] = parent[parent[e]];
        return parent[e];
    }
public:
    int removeStones(vector<vector<int>>& stones)
    {
        parent.resize(stones.size());
        for(int i=0; i<stones.size(); i++)
        {
            int row = stones[i][0];
            int col = stones[i][1];
            bool isRow = (row2root.find(row) != row2root.end());
            bool isCol = (col2root.find(col) != col2root.end());
            if(!isRow && !isCol)
            {
                col2root[col] = row2root[row] = parent[i] = i;
            }
            else if(isRow && !isCol)
            {
                col2root[col] = row2root[row] = parent[i] = root(row2root[row]);
            }
            else if(!isRow && isCol)
            {
                col2root[col] = row2root[row] = parent[i] = root(col2root[col]);
            }
            else // union
            {
                int rootCol = root(col2root[col]);
                int rootRow = root(row2root[row]);
                parent[i] = parent[rootCol] = col2root[col] = rootRow;
            }
        }
        int ret = stones.size();
        for(int i=0; i<stones.size(); i++)
            if(parent[i] == i)
                ret--;
        return ret;
    }
};
