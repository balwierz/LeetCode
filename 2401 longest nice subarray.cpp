class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) 
    {
        int n = nums.size(), left = 0, right = 0, mask = 0, ret = 1;
        while(right < n)
        {
            while(right < n && (mask & nums[right]) == 0)
                mask |= nums[right++];
            ret = max(ret, right-left);
            while(right < n && (mask & nums[right]))
                mask &= ~nums[left++];
        }
        return ret;
    }
};
