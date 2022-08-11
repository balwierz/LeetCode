class Solution {
public:
    long long minimumReplacement(vector<int>& nums)
    {
        auto it=nums.rbegin();
        int prev = *it;
        it++;
        long long ret = 0;
        for(; it!=nums.rend(); it++)
        {
            if(*it <= prev)
            {
                prev = *it;
                continue;
            }
            int nBins = (*it + prev - 1) / prev;
            prev = *it / nBins;
            ret += nBins - 1;
        }
        return ret;
    }
};
