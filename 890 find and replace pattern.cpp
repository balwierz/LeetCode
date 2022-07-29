class Solution {
    bool isPermutation(string &a, string &b)
    {
        unordered_map<char, char> a2b, b2a;
        for(int i=0; i<a.size(); ++i)
        {
            auto abI = a2b.find(a[i]);
            auto baI = b2a.find(b[i]);
            if(abI == a2b.end() && baI == b2a.end())
            {
                // this letter pair does not exist in dicts
                a2b[a[i]] = b[i];
                b2a[b[i]] = a[i];
                continue;
            }
            if(abI != a2b.end() && baI != b2a.end() &&
               abI->second == b[i] && baI->second == a[i])
            {} // nop
            else
                return false;
        }
        return true;
    }
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern)
    {
        // bijection as two maps
        vector<string> ret;
        for(auto word : words)
        {
            if(isPermutation(word, pattern))
                ret.push_back(word);
        }
        return ret;
    }
};
