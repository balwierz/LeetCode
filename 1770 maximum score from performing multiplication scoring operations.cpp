    int maximumScore(vector<int>& nums, vector<int>& multipliers)
    {
        int numN = nums.size();
        int mulN = multipliers.size();
        vector<int> dp(mulN+1, 0);
        for(int op=mulN-1; op>=0; op--)
            for(int left=0; left<=op; left++)
                dp[left] = max(dp[left]   + nums[numN-1-op+left] * multipliers[op],
                               dp[left+1] + nums[left] * multipliers[op]);
        return dp[0];
    }
