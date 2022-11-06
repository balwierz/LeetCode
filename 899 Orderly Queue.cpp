class Solution {
public:
    string orderlyQueue(string s, int k)
    {
        if(k > 1)
        {
            sort(s.begin(), s.end());
            return s;
        }
        int n = s.size();
        s += s;
        string ret = {(char)255, 0};
        for(int i=0; i<n; i++)
        {
            string window = s.substr(i, n);
            if(window < ret)
                ret = window;
        }
        return ret;
    }
};
