class Solution {
public:
    int maxProfit(vector<int>& prices)
    {
        int none[2], one[2], cool[2];
        int n = prices.size();
        none[0] = 0; one[0] = -5000000; cool[0] = -5000000;
        int curr = 0;
        for(int i = 0; i<n; i++, curr = 1-curr)
        {
            none[1-curr] = max(none[curr], cool[curr]);
            cool[1-curr] = one[curr]+prices[i];
            one[1-curr]  = max(none[curr]-prices[i], one[curr]);
        }
        return max(none[curr], cool[curr]);
    }
};
