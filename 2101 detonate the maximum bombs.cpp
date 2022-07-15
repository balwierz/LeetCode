#define X 0
#define Y 1
#define R 2

class Solution {
    //vector<vector<bool>> adj;
    vector<vector<int>> neigh;
    int n;
    int dfs(int i, vector<bool> &visited)
    {
        if(visited[i])
            return 0;
        int ans = 1;
        visited[i] = true;
        for(int nn : neigh[i])
        {
            ans += dfs(nn, visited);
        }
        return ans;
    }
public:
    int maximumDetonation(vector<vector<int>>& bombs)
    {
        n = bombs.size();
        //adj = vector<vector<bool>>(n, vector<bool>(n, false));
        neigh = vector<vector<int>>(n, vector<int>(0));
        for(int i=0; i<n-1; i++)
            for(int j=i+1; j<n; j++)
            {
                long int x = bombs[i][X]-bombs[j][X];
                long int y = bombs[i][Y]-bombs[j][Y];
                long int r1 = bombs[i][R];
                long int r2 = bombs[j][R];
                x *= x;
                y *= y;
                r1 *= r1;
                r2 *= r2;
                if(x + y <= r1)
                    neigh[i].push_back(j);
                if(x + y <= r2)
                    neigh[j].push_back(i);
            }
        int ans = 1;
        for(int i=0; i<n; i++)
        {
            vector<bool> visited(n, false);
            int t = dfs(i, visited);
            ans = max(ans, t);
        }
        return ans;
    }
};
