// could be solved with formula ceil(log_{rounds+1}buckets)

class Solution {
    
    int newton(int n, int k)
    {
        static int newtonMemo[100][100];
        //if(k < n)
        //    return 0;
        if(k == 0 || n == k)
            return 1;
        if(newtonMemo[n][k])
            return newtonMemo[n][k];
        int ret = newton(n-1, k) + newton(n-1, k-1);
        newtonMemo[n][k] = ret;
        return ret;
    }
    int maxBuckets(int nPigs, int nRounds)
    {
        static int bucketMemo[100][101];
        if(nRounds == 1)
            return (1 << nPigs);
        if(bucketMemo[nPigs][nRounds])
            return bucketMemo[nPigs][nRounds];
        int ret = 0;
        for(int intersection=0; intersection<=nPigs; intersection++)
            ret += newton(nPigs, intersection) * maxBuckets(nPigs-intersection, nRounds-1);
        bucketMemo[nPigs][nRounds] = ret;
        return ret;
    }
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest)
    {
        int nRounds = minutesToTest / minutesToDie;
        // find the num of pigs:
        int nPigs=0;
        for(; 1; nPigs++)
        {
            if(maxBuckets(nPigs, nRounds) >= buckets)
                return nPigs;
        }
    }
};
