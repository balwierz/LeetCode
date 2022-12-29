class Solution {
public:
    int longestSquareStreak(vector<int>& nums) 
    {
        unordered_set<long> s;
        for(int v : nums)
            s.insert(v);
        int ret = 1;
        for(int v : nums)
        {
            int k = 1;
            while(s.count((long)v*v))
            {
                k++;
                v *= v;
            }
            ret = max(ret, k);
        }
        return ret == 1 ? -1 : ret;
    }
};
