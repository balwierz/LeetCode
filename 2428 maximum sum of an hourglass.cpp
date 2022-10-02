class Solution {
public:
    int maxSum(vector<vector<int>>& grid)
    {
        int m = grid.size();
        int n = grid[0].size();
        int ret = 0;
        for(int r=0; r<=m-3; r++)
            for(int c=0; c<=n-3; c++)
            {
                int a = grid[r][c] + grid[r][c+1] + grid[r][c+2]+
                                     grid[r+1][c+1] +
                        grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2];
                ret = max(ret, a);
            }
        return ret;
    }
};
