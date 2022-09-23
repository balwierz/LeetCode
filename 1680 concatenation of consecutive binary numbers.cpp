int mostSigBit(int n)
{
    // calculate the  number
    // of leading zeroes
    int k = __builtin_clz(n);
 
    // position of the most
    // significant digit:
    return sizeof(int)*8 - k;
}

long long MOD = 1e9+7;
class Solution {
public:
    int concatenatedBinary(int n)
    {
        long long ret = 0;
        for(int i=1; i<=n; i++)
        {
            int iLen = mostSigBit(i);
            ret <<= iLen;
            ret += i;
            ret %= MOD;
        }
        return ret;
    }
    
};
