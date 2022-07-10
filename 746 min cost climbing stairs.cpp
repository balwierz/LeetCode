class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) 
    {
        int n = cost.size();
        vector<int> x(n);
        x[0] = cost[0];
        x[1] = cost[1];
        for(int i=2; i<n; i++)
        {
            x[i] = cost[i] + min(x[i-1], x[i-2]);
        }
        return(min(x[n-1], x[n-2]));
    }
};
