class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target)
    {
        sort(nums.begin(), nums.end());
        int best = 100000;
        int ret = 0;
        for(int i=0; i<nums.size()-2; i++)
        {
            int j=i+1, k=nums.size()-1;
            while(j<k)
            {
                int sum = nums[i] + nums[j] + nums[k];
                int score = abs(target - sum);
                if(score == 0)
                    return sum;
                if(score < best)
                {
                    best = score;
                    ret = sum;
                }
                if(target < sum)
                    k--;
                else
                    j++;
            }
        }
        return ret;
    }
};
