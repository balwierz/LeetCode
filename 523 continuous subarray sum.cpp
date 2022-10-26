class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k)
    {
        int val = 0;
        unordered_map<int, int> seen;
        seen[0] = -1;
        for(int i=0; i<nums.size(); i++)
        {
            val = (val + nums[i]) % k;
            auto firstPos = seen.find(val);
            if(firstPos != seen.end())
                if(firstPos->second < i-1)
                    return true;
                else {}
            else
                seen[val] = i;
        }
        return false;
    }
};
