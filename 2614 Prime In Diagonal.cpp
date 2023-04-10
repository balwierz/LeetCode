class Solution {
public:
    vector<bool> ints;
    Solution()
    {
        int maxs = 4000002;
        ints.resize(maxs, true);
        ints[1] = false;
        int e = sqrt(maxs);
        for(int i = 2; i<e; i++)
            if(ints[i])
                for(int j=i+i; j<maxs; j+=i)
                    ints[j] = false;
    }
    int diagonalPrime(vector<vector<int>>& nums) 
    {
        int ret = 0;
        for(int i=0; i<nums.size(); i++)
        {
            if(ints[nums[i][i]])
                ret = max(ret, nums[i][i]);
            if(ints[nums[i][nums.size() -1 -i]])
                ret = max(ret, nums[i][nums.size() -1 -i]);
        }
        return ret;
    }
};
