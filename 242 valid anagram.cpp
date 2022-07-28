class Solution {
public:
    bool isAnagram(string s, string t)
    {
        unordered_multiset<char> ms;
        for(char c : s)
            ms.insert(c);
        for(char c : t)
        {
            auto it = ms.find(c);
            if(it != ms.end())
                ms.erase(it);
            else
                return false;
        }
        if(ms.empty())
            return true;
        return false;
    }
};
