class Solution {
public:
    int rearrangeSticks(int n, int k)
    {
        int mod = 1000000007;
        static int memo[1001][1001];
        if(n==0 && k==0)
            return 1;
        if(k>n || k==0)
            return 0;
        if(memo[n][k])
            return memo[n][k];
        int ret = rearrangeSticks(n-1, k-1);  // smallest stick is first
        ret += ((long long)(n-1) * rearrangeSticks(n-1, k)) % mod;
        ret %= mod;
        memo[n][k] = ret;
        return ret;
    }
    
    int rearrangeSticks2(int n, int k) // too slow for n=481, k=314
    {
        static int memo[1001][1001];
        if(n==0 && k==0)
            return 1;
        if(k>n || k==0)
            return 0;
        if(memo[n][k])
            return memo[n][k];
        int ret = 0;
        for(int i=1; i<=n; i++)
        {
            unsigned long long coef = 1;
            for(int j=n-i+1; j<=n-1; j++)
            {
                coef *= j;
                coef %= 1000000007;
            }
            long long tmp = rearrangeSticks(n-i, k-1) * coef;
            tmp %= 1000000007;
            ret += tmp;
            ret %= 1000000007;
        }
        memo[n][k] = ret;
        return ret;
    }
};
