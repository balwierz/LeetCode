int mod = 1000000007;
class Solution {
public:
    int countVowelPermutation(int n)
    {
        vector<long long> num(128,0);
        num['a'] = 1;
        num['e'] = 1;
        num['i'] = 1;
        num['o'] = 1;
        num['u'] = 1;
        for(int i=1; i<n; i++)
        {
            vector<long long> nn(128,0);
            nn['a'] = ((num['e'] + num['i']) % mod + num['u']) % mod ;
            nn['e'] = (num['a'] + num['i']) % mod;
            nn['i'] = (num['e'] + num['o']) % mod;
            nn['o'] = num['i'];
            nn['u'] = (num['i'] + num['o']) % mod;
            num = nn;
        }
        return (((((num['a'] + num['e']) % mod + num['i']) % mod) + 
            num['o']) % mod + num['u']) % mod;
    }
};
