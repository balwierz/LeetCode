class Solution {
public:
    long long countBadPairs(vector<int>& nums)
    {
        unordered_map<int, int> strata2count;
        for(int i=0; i<nums.size(); ++i)
            strata2count[nums[i] - i]++;
        long long ret = (nums.size() * (nums.size()-1));  // number of all possible pairs * 2
        for(auto &p:strata2count)
            ret -= ((long long)p.second * (p.second-1));
        return ret/2;
    }
};
