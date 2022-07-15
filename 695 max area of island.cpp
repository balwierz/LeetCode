class Solution
{
    vector<vector<int>> *grid2;
    int m, n;
    vector<vector<bool>> visited;
    int dfs(int i, int j)
    {
        if(i<0 || j<0 || i>=m || j>=n)
            return 0;
        if(visited[i][j] || (*grid2)[i][j] == 0)
            return 0;
        int ret = 1;
        visited[i][j] = true;
        ret += dfs(i-1, j);
        ret += dfs(i+1, j);
        ret += dfs(i,   j-1);
        ret += dfs(i,   j+1);
        return ret;
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid)
    {
        int maxIsland = 0;
        m = grid.size();
        n = grid[0].size();
        grid2 = &grid;
        visited = vector<vector<bool>>(m, vector<bool>(n, false));
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
            {
                if(grid[i][j] == 1)
                {
                    int area = dfs(i, j);
                    if(area > maxIsland)
                        maxIsland = area;
                }
            }
        return maxIsland;
    }
};
