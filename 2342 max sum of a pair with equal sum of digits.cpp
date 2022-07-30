class Solution {
    int num2sum(int num)
    {
        int ret = 0;
        while(num)
        {
            ret += num % 10;
            num /= 10;
        }
        return ret;
    }
    
public:
    int maximumSum(vector<int>& nums)
    {
        unordered_multiset<int> sums[82];
        for(int &num:nums)
        {
            sums[num2sum(num)].insert(num);
        }
        int best = -1;
        for(auto &numSet:sums)
        {
            if(numSet.size() >= 2)
            {
                int max = 0;
                for(int n:numSet)
                    if(n>max)
                        max = n;
                int max2 = 0;
                numSet.extract(max);
                for(int n:numSet)
                    if(n>max2)
                        max2 = n;
                if(best < max + max2)
                    best = max + max2;
            }
        }
        return best;
    }
};
