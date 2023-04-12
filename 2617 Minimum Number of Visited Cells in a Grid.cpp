class Solution {
public:

    int minimumVisitedCells(vector<vector<int>>& grid) 
    {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dCol(m, vector<int>(n, 1e6));
        dCol[0][0] = 1;
        int d = 1e6;
        for (int i = 0; i < m; ++i) 
        {
            vector<int> dRow(n, 1e6);
            for (int j = 0; j < n; ++j) 
            {
                d = min(dCol[i][j], dRow[j]);
                for (int x = min(grid[i][j] + i, m-1); x > i && dCol[x][j] > d; --x)
                    dCol[x][j] = d + 1;
                for (int x = min(grid[i][j] + j, n-1); x > j && dRow[x] > d; --x) 
                    dRow[x] = d + 1;
            }
        }
        return d == 1e6 ? -1 : d;
    }

  
    int minimumVisitedCells7(vector<vector<int>>& grid) 
    {
        const int inf = 99999999;
        int m = grid.size();
        int n = grid[0].size();
        int dist = inf;
        vector<priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>>> colPq(n);
        colPq[0].push({0, 0});
        for(int i=0; i<m; i++)
        {
            priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> rowPq;
            for(int j=0; j<n; j++)
            {
                int colBestVal = inf;
                while(colPq[j].size())
                {
                    const pair<int,int> &cur = colPq[j].top();
                    if(cur.second < i)
                        colPq[j].pop();
                    else
                    {
                        colBestVal = cur.first + 1;
                        break;
                    }
                }
                int rowBestVal = inf;
                while(rowPq.size())
                {
                    const pair<int,int> &cur = rowPq.top();
                    if(cur.second < j)
                        rowPq.pop();
                    else
                    {
                        rowBestVal = cur.first + 1;
                        break;
                    }
                }
                dist = min(colBestVal, rowBestVal);
                if(dist < inf)
                {
                    colPq[j].push({dist, i+grid[i][j]});
                    rowPq.push({dist, j+grid[i][j]});
                }
            }
        }
        return dist == inf ? -1 : dist;
    }
};
