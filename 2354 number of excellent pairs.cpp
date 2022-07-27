class Solution {
    int pop(unsigned x)
    {
        x = x - ((x >> 1) & 0x55555555);
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
        x = (x + (x >> 4)) & 0x0F0F0F0F;
        x = x + (x >> 8);
        x = x + (x >> 16);
        return x & 0x0000003F;
    }
public:
    long long countExcellentPairs(vector<int>& nums, int k)
    {
        // remove repeated values
        unordered_set<int> numSet(nums.begin(), nums.end());
        
        // count bits
        vector<int> c(33, 0);
        for(auto n : numSet)
            //c[popcount(n)]++;   // C++20
            c[pop(n)]++;            
        
        long long ret = 0;
        for(int i=0; i<=32; i++)
            for(int j=max(k-i, 0); j<=32; j++)
                ret += ((long long) c[i]) * c[j];
        
        return ret;
    }
};
