class Solution {
    void dfs(vector<vector<char>> &g, int i, int j, int m, int n)
    {
        g[i][j] = '0';
        if(i>0 && g[i-1][j] == '1')
            dfs(g, i-1, j, m, n);
        if(i<m-1 && g[i+1][j] == '1')
            dfs(g, i+1, j, m, n);
        if(j>0 && g[i][j-1] == '1')
            dfs(g, i, j-1, m, n);
        if(j<n-1 && g[i][j+1] == '1')
            dfs(g, i, j+1, m, n);
    }
public:
    int numIslands(vector<vector<char>>& grid)
    {
        int ret = 0;
        int m = grid.size(), n = grid[0].size();
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
                if(grid[i][j] == '1')
                {
                    dfs(grid, i, j, m, n);
                    ret++;
                }
        return ret;
    }
};
