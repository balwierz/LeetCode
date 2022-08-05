class Solution {
public:
    int combinationSum4(vector<int>& nums, int target)
    {
        unsigned long int comb[target+1];
        comb[0] = 1;
        for(int i = 1; i<=target; i++)
        {
            comb[i] = 0;
            for(int num:nums)
            {
                if(num <= i)
                    comb[i] += comb[i-num];
            }
        }
        return comb[target];
    }
};
