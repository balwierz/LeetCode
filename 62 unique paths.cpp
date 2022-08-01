class Solution {
    int newton(int n, int k)
    {
        static int memo[202][101];
        if(k==0 || k==n)
            return 1;
        if(memo[n][k])
            return memo[n][k];
        memo[n][k] = newton(n-1, k) + newton(n-1, k-1);
        return(memo[n][k]);
    }
    int newton2(int n, int k)
    {
        double ret = 1;
        for( double i = 1; i <= k; i++)
             ret *= (( n - i + 1 ) / i);
        return (ret+0.5);
    }
public:
    int uniquePaths(int m, int n)
    {
        return newton2(m+n-2, m-1);
    }
};
