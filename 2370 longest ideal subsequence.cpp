class Solution {
public:
    int longestIdealString(string s, int k)
    {
        int v[256] = {0};
        for(char c:s)
        {
            int w = 0;
            for(int i=c-k; i<=c+k; ++i)
                w = max(w, v[i]);
            v[c] = w + 1;
        }
        int ret = 0;
        for(int i='a'; i<='z'; ++i)
            if(ret < v[i])
                ret = v[i];
        return ret;
    }
};
