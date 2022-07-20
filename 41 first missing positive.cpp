class Solution {
public:
    int firstMissingPositive(vector<int>& nums)
    {
        // we are going to destroy nums.
        int n = nums.size();
        for(int s=0; s<nums.size(); s++) // left slider
        {
            if(nums[s] <= 0 || nums[s] > n)
            {
                nums[s] = 0;
                continue;
            }
            if(nums[s] == s+1) // we have seen this number or we are just seeing it but it is already placed where it should
            {continue;}
            int it = s;
            int oldval = 0;
            while(true)
            {
                if(nums[it] == it+1)
                    break;
                if(nums[it] <= 0 || nums[it] > n)
                {
                    nums[it] = oldval;
                    break;
                }
                int tmp = nums[it];
                nums[it] = oldval; // 
                it = tmp-1;
                oldval = tmp;
                
            }
        }
        //for(auto a:nums)
        //    cout << a << " ";
        for(int i=0; i<n; i++)
        {
            if(nums[i] == 0)
                return i+1;
        }
        return n+1;
    }
};
