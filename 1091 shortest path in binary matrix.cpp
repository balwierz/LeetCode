class Elem
{
    public:
    int x, y, dist;
    Elem(int x, int y, int dist) : x(x), y(y), dist(dist) {}
};
class Solution 
{
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid)
    {
        int n = grid.size();
        if(grid[0][0] == 1 || grid[n-1][n-1] == 1)
            return -1;
        deque<Elem> q;
        q.emplace_back(0,0,0);
        grid[0][0] = 1;
        while(! q.empty())
        {
            auto e = q.front();
            //cout << e.x << " " << e.y << " " << e.dist << endl;
            q.pop_front();
            if(e.x == n-1 && e.y == n-1)
                return e.dist+1;
            if(e.x > 0)
            {
                if(grid[e.x-1][e.y] == 0)
                {
                    q.emplace_back(e.x-1, e.y, e.dist+1);
                    grid[e.x-1][e.y] = 1;
                }
                if(e.y > 0)
                {
                    if(grid[e.x-1][e.y-1] == 0)
                    {
                        q.emplace_back(e.x-1, e.y-1, e.dist+1);
                        grid[e.x-1][e.y-1] = 1;
                    }
                }
                if(e.y < n-1)
                {
                    if(grid[e.x-1][e.y+1] == 0)
                    {
                        q.emplace_back(e.x-1, e.y+1, e.dist+1);
                        grid[e.x-1][e.y+1] = 1;
                    }
                }
            }
            if(e.x < n-1)
            {
                if(grid[e.x+1][e.y] == 0)
                {
                    q.emplace_back(e.x+1, e.y, e.dist+1);
                    grid[e.x+1][e.y] = 1;
                }
                if(e.y > 0)
                {
                    if(grid[e.x+1][e.y-1] == 0)
                    {
                        q.emplace_back(e.x+1, e.y-1, e.dist+1);
                        grid[e.x+1][e.y-1] = 1;
                    }
                }
                if(e.y < n-1)
                {
                    if(grid[e.x+1][e.y+1] == 0)
                    {
                        q.emplace_back(e.x+1, e.y+1, e.dist+1);
                        grid[e.x+1][e.y+1] = 1;
                    }
                }
            }
            if(e.y > 0 && grid[e.x][e.y-1] == 0)
            {
                q.emplace_back(e.x, e.y-1, e.dist+1);
                grid[e.x][e.y-1] = 1;   
            }
            if(e.y < n-1 && grid[e.x][e.y+1] == 0)
            {
                q.emplace_back(e.x, e.y+1, e.dist+1);
                grid[e.x][e.y+1] = 1;
            }
        } // while q not empty
        return -1;
    }
};
