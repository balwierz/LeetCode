class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word)
    {
        int ret = 0;
        for(auto &p : patterns)
        {
            if(word.find(p) != string::npos)
                ret++;
        }
        return ret;
    }
};
