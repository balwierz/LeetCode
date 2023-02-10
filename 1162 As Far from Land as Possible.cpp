class XY
{
    public:
    int x, y;
    XY(int &xx, int &yy) : x(xx), y(yy) {}
    bool operator==(const XY &other) const
    {
        return x==other.x && y==other.y;
    }
    bool operator<(const XY &other) const
    {
        return (x < other.x) ? true : (y < other.y ? true : false);
    }
};
template<>
struct std::hash<XY>
{
    std::size_t operator()(const XY &xy) const noexcept
    {
        return xy.x & (xy.y<<8);
    }
};

class Solution2 {
public:
    int maxDistance(vector<vector<int>>& grid)
    {
        int n = grid.size();
        set<XY> q;
        int numUnvisited = n*n;
        // init
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                if(grid[i][j])
                {
                    q.insert(XY(i,j));
                    grid[i][j] = true;
                    numUnvisited --;
                }
        if(numUnvisited == 0 || numUnvisited == n*n)
            return -1;
        int step = 0;
        vector<vector<int>> direction({{-1,0}, {1,0}, {0,-1}, {0,1}});
        while(numUnvisited)
        {
            //cout << numUnvisited << endl;
            set<XY> newSet;
            step++;
            for(auto &pos : q)
            {
                for(const vector<int> &dir : direction)
                {
                    int x = pos.x + dir[0];
                    int y = pos.y + dir[1];
                    if(x>=0 && x<n && y>=0 && y<n && !grid[x][y])
                    {
                        newSet.insert(XY(x,y));
                        grid[x][y] = 1;
                    }
                }
            }
            numUnvisited -= newSet.size();
            q = newSet;
        }
        return step;
    }
};


class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size(), res = 0, dp[n][n];
        memset(dp, 0, sizeof(dp));
        
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                if(grid[i][j] == 1) 
                    continue;
                dp[i][j] = 1e3;
                if(i - 1 >= 0)
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1);
                if(j - 1 >= 0)
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1);
            }
        }
        
        
        for(int i = n - 1; i >= 0; --i) {
            for(int j = n - 1; j >= 0; --j) {
                if(grid[i][j] == 1)
                    continue;
                if(i + 1 < n)
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1);
                if(j + 1 < n)
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1);
                res = max(res, dp[i][j]);
            }
        }
        return (res == 0 || res == 1e3) ? -1 : res;
    }
};
