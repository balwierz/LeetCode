class Solution {
public:
    int commonFactors(int a, int b)
    {
        int l = max(a, b);
        int ret = 1;
        for(int i=2; i<=l; i++)
        {
            if(a % i == 0 && b % i == 0)
                ret++;
        }
        return ret;
    }
};
