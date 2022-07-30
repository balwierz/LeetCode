class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long ret = 0LL;
        long long cur = 0;
        for(int a:nums)
            if(a)
                cur = 0LL;
            else
                ret += ++cur;
        return ret;
    }
};
