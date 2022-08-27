class Solution {
public:
    static auto max(long long a, long long b)
    {
        return (a < b ? b : a);
    }
    static auto min(long long a, long long b)
    {
        return a < b ? a : b;
    }
    long long maxPoints(vector<vector<int>>& points)
    {
        int m = points.size(), n = points[0].size();
        vector<long long> dp(points[0].begin(), points[0].end());
        long long dpRange = accumulate(dp.begin(), dp.end(), INT_MIN, max) - 
            accumulate(dp.begin(), dp.end(), INT_MAX, min) + 1;
        for(int i=1; i<m; i++)
        {
            vector<long long> dpNew(n);
            long long dpMin = INT_MAX;
            long long dpMax = INT_MIN;
            for(int j=0; j<n; j++)
            {
                long long val = 0;
                int bestI = 0;
                for(int j2=max(0, j-dpRange); j2<min(n, j+dpRange); j2++)
                {
                    long long f = dp[j2] - abs(j2-j);
                    if(f > val)
                    {
                        val = f;
                        bestI = j2;
                    }
                }
                dpNew[j] = val + points[i][j];
                dpMax = max(dpMax, dpNew[j]);
                dpMin = min(dpMin, dpNew[j]);
                while(j<bestI)
                {
                    ++j;
                    dpNew[j] = points[i][j] + dp[bestI] - (bestI-j);
                    dpMax = max(dpMax, dpNew[j]);
                    dpMin = min(dpMin, dpNew[j]);
                }   
            }
            dp = dpNew;
            dpRange = dpMax - dpMin + 1;
            //cout << "dpRange " << dpRange << endl;
        }

        long long ret = accumulate(dp.begin(), dp.end(), 0LL, max);
        return ret;
    }
};
