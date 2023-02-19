class Solution {
public:
    int minImpossibleOR(vector<int>& nums)
    {
        int mask = 0;
        for(int &a : nums)
            if(__builtin_popcount(a) == 1)
                mask |= a;
        for(int i=1; true; i <<= 1)
            if((mask & i) == 0)
                return i;
    }
};
