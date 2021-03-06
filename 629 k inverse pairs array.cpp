const int MOD = 1e9+7;
class Solution {
    vector<vector<int>> tab;
    int helper(int n, int k)
    {
        //cout << "helper " << n << " " << k << endl;
        //if(k < 0)
        //    return 0;

        if(k > n*(n-1)/2) 
        {
            //cout << "wrong n=" << n << " k=" << k << endl;
            //tab[n][k] = 0;
            return 0;
        }
        if(k == 0)
            return 1;
        if(n == 1)
            return 1;
        if(tab[n][k] != -1)
            return tab[n][k];
        int ret = 0;
        /*for(int i=0; i<n && k-i>=0; i++)  // how many positions does the largest number jump
        {
            int tmp = helper(n-1, k-i);
            ret += tmp;
            ret %= MOD;
            //cout << "it " << n-1 << " " << k-i << " tmp " << tmp << endl;
        }*/
        ret += helper(n, k-1);
        ret += helper(n-1, k);
        ret %= MOD;
        ret -= (k-n >= 0) ? helper(n-1, k-n) : 0;
        ret += MOD;
        ret %= MOD;
        //cout << "a" << endl;
        tab[n][k] = ret;
        //cout << "b" << endl;
        //cout << "n" << n << " k" << k << " " << ret << endl;
        return ret;
    }
public:
    int kInversePairs(int n, int k)
    {
        //int tab[n+1][k+1];
        tab = vector<vector<int>>(n+1, vector<int>(k+1, -1));
        tab[1][0] = 1;
       // cout << "foo" << endl;
        //memset(tab, -1, sizeof(tab));
        return helper(n, k);
    }
};
