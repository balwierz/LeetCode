int inf = 10000*100+1;

class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target)
    {
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(target+1, inf)));
        if(m == 0)
        {
            return -1;
        }
        // init k=1, i=0, j=0..n-1
        //cout << "    k=1" << endl;
        if(houses[0] == 0)
        {
            for(int j=0; j<n; j++)
                dp[0][j][1] = cost[0][j];
        }
        else // already painted
        {
            for(int j=0; j<n; j++)
            {
                if(j+1 == houses[0])
                    dp[0][j][1] = 0; //cost[0][j];
                else
                    dp[0][j][1] = inf;
            }
        }
        //for(int j=0; j<n; j++)
        //    cout << dp[0][j][1] << ' ';
        //cout << endl;
        // init k=2..target, i=0, j=0..n-1
        for(int k=2; k<=target; k++)
            for(int j=0; j<n; j++)
                dp[0][j][k] = inf;
        // loop over houses
        for(int i=1; i<m; i++)
        {
            //cout << "i=" << i << endl;
            // k=1, can only extend the k=1 neighbourhood
            //cout << "    k=" << 1 << endl;
            if(houses[i] == 0)
            {
                for(int j=0; j<n; j++)
                    dp[i][j][1] = dp[i-1][j][1] + cost[i][j];
            }
            else // already painted
            {
                for(int j=0; j<n; j++)
                {
                    if(j+1 == houses[i])
                        dp[i][j][1] = dp[i-1][j][1]; // + cost[i][j];
                    else
                        dp[i][j][1] = inf;
                }
            }
            //for (int j=0; j<n; j++)
             //   cout << dp[i][j][1] << ' ';
            //cout << endl;
            // k=2..
            for(int k=2; k<=target; k++)
            {
                //cout << "    k=" << k << endl;
                if(houses[i] == 0)
                {
                    for(int j=0; j<n; j++)
                    {
                        //cout << "        j=" << j << endl;
                        int min=inf;
                        for(int jprim=0; jprim<n; jprim++)  // loop over the previous colour
                        {
                            if(jprim == j)
                            {
                                // extend the current neighbourhood keeping k
                                int thisval = dp[i-1][j][k] + cost[i][j];
                                if(thisval < min)
                                    min = thisval;
                            }
                            else
                            {
                                // we create the new neighbourhood
                                int thisval = dp[i-1][jprim][k-1] + cost[i][j];
                                if(thisval < min)
                                    min = thisval;
                            }
                        }
                        dp[i][j][k] = min;
                        //cout << min << endl;
                    }
                }
                else
                {
                    // already painted
                    for(int j=0; j<n; j++)
                    {
                        if(j+1 == houses[i])
                        {
                            int min=inf;
                            for(int jprim=0; jprim<n; jprim++)
                            {
                                if(jprim == j)
                                {
                                    int thisval = dp[i-1][j][k]; // + cost[i][j];
                                    if(thisval < min)
                                        min = thisval;
                                }
                                else
                                {
                                    // we create the new neighbourhood
                                    int thisval = dp[i-1][jprim][k-1]; // + cost[i][j];
                                    if(thisval < min)
                                        min = thisval;
                                }
                            }
                            dp[i][j][k] = min;
                        }
                        else 
                        {
                            dp[i][j][k] = inf;
                        }
                    }
                }
                //for(int j=0; j<n; j++)
                //    cout << dp[i][j][k] << " ";
                //cout << endl;
            }
        }
        // find the lowest value in i=m-1; j=0..n-1, k=target
        int min = inf;
        for(int j=0; j<n; j++)
            if(dp[m-1][j][target] < min)
                min = dp[m-1][j][target];
        if(min != inf)
            return min;
        else return -1;
    }
};
