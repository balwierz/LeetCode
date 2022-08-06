class Solution {
public:
    int subsetXORSum(vector<int>& nums)
    {
        int ored = 0;
        for(int n:nums)
            ored |= n;
        return ored * pow(2, nums.size() - 1);
    }
    int subsetXORSum2(vector<int>& nums)
    {
        vector<int> ret(1, 0);
        for(int n:nums)
        {
            int size = ret.size();
            for(int i=0; i<size; ++i)
                ret.push_back(ret[i]^n);
        }
        return accumulate(ret.begin(), ret.end(), 0);
    }
};
