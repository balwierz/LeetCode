    int numberOfPaths(vector<vector<int>>& grid, int k)
    {
        int m = grid.size(), n=grid[0].size();
        vector<vector<vector<int>>> tab(m, vector<vector<int>>(n, vector<int>(k, 0)));
        tab[0][0][grid[0][0] % k] = 1;
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
            {
                auto &t = tab[i][j];
                if(i!=0)
                {
                    for(int a=0; a<k; a++)
                    {
                        t[(grid[i][j] + a) % k] += tab[i-1][j][a];
                        t[(grid[i][j] + a) % k] %= 1000000007;
                    }
                }
                if(j!=0)
                {
                    for(int a=0; a<k; a++)
                    {
                        t[(grid[i][j] + a) % k] += tab[i][j-1][a];
                        t[(grid[i][j] + a) % k] %= 1000000007;
                    }
                }
            }
        return tab[m-1][n-1][0];
    }
