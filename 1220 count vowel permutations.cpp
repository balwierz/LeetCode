int mod = 1000000007;
class Solution {
public:
    int countVowelPermutation(int n)
    {
        long a = 1, e = 1, i = 1, o = 1, u = 1;
        for(int j=1; j<n; j++)
        {
            long na = (e + i + u) % mod ;
            long ni = (e + o) % mod;
            e = (a + i) % mod;
            u = (i + o) % mod;
            o = i;
            a = na;
            i = ni;
        }
        return (a + e + i + o + u) % mod;
    }
};
