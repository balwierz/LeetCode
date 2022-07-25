class Solution {
    int search(vector<int>&n, float t, int i, int j)
    {
        while(i<j)
        {
            int k = i + (j-i) / 2;
            if(n[k] == t)
                return k;
            if(t < n[k])
                j = k;
            else
                i = k+1;
        }
        return i;
    }
public:
    vector<int> searchRange(vector<int>& nums, int target)
    {
        int i = search(nums, target-0.5, 0, nums.size());
        if(i == nums.size())
            return vector<int> {-1, -1};
        if(nums[i] != target)
            return vector<int> {-1, -1};
        int j = search(nums, target+0.5, i, nums.size());
        return vector<int> {i, j-1};
    }
};
