class Solution {
public:
    int similarPairs(vector<string>& words)
    {
        unordered_map<int, int> code2count;
        for(auto w : words)
        {
            int code = 0;
            for(char c : w)
            {
                code |= 1 << (c-'a');
            }
            code2count[code] ++;
        }
        int ret = 0;
        for(auto &p : code2count)
        {
            ret += p.second * (p.second - 1) / 2;
        }
        return ret;
    }
};
