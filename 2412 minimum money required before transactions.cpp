class Solution {
public:
    long long minimumMoney(vector<vector<int>>& txn)
    {
        long long sumDelta = 0;
        vector<pair<long long, long long>> tmp;
        long long biggestGain = 0;
        for(vector<int>&v : txn)
        {
            long long cost = -v[0];
            long long delta = v[1] - v[0];
            if(delta < 0) // for sure the delta partwill take place in the score
                sumDelta += delta;
            if(delta > 0) // we don't sum delta;
                delta = 0;
            tmp.emplace_back(cost, delta);
        }
        for(auto &[cost, delta] : tmp)
        {
            // among all the elements in 
            long long gain = - delta + cost + sumDelta;
            if(gain < biggestGain)
                biggestGain = gain;
        }
        return -biggestGain;
    }
};
