class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr)
    {
        sort(arr.begin(), arr.end());
        int ret = 0;
        // identify all pairs of forming valid multiplication
        unordered_map<int,int> s;   // value to index;
        for(int i=0; i<arr.size(); ++i)
            s[arr[i]] = i;
        vector<long long int> nWays(arr.size(), 1);   // init node itself, no children
        forward_list<pair<int,int>> multiplications[arr.size()];
        for(int i=0; i<arr.size(); i++)
        {
            for(int j=i; j<arr.size(); j++)
            {
                long long int m = (long long)arr[i] * arr[j];
                if(m > arr[arr.size()-1])
                    break;
                if(s.count(m))
                {
                    multiplications[s[m]].emplace_front(i,j);
                }
            }
        }
        for(int i=0; i<arr.size(); i++)
        {
            for(auto &[a,b] : multiplications[i])
            {
                int symmetry = a==b ? 1 : 2;
                nWays[i] += symmetry * nWays[a] * nWays[b];
                nWays[i] %= 1000000007;
            }
        }
        for(int a:nWays)
        {
            ret += a;
            ret %= 1000000007;
        }
        return ret;
    }
};
