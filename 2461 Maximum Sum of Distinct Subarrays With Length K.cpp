class Solution {
    int numBad;
    unordered_map<int,int> count;
    long long bestSum;
    long long sum;
            
    bool add(int num)
    {
        if(count[num] == 1)
            numBad++;
        sum += num;
        count[num] ++;
        return numBad == 0;
    }
    
    bool remove(int num)
    {
        if(count[num] == 2)
            numBad --;
        sum -= num;
        count[num]--;
        return numBad == 0;
    }
public:
    Solution()
    {
        sum = 0;
        numBad = 0;
        bestSum = 0;
    }

    long long maximumSubarraySum(vector<int>& nums, int k)
    {
        int i=0;
        for(; i<k; i++)
            add(nums[i]);
        if(!numBad)
            bestSum = sum;
        for(; i<nums.size(); i++)
        {
            remove(nums[i-k]);
            if(add(nums[i]))
                bestSum = max(bestSum, sum);
        }
        return bestSum;
    }
};
