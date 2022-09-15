class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) 
    {
        vector<int> ret;
        multiset<int> s(changed.begin(), changed.end());
        if(s.count(0) % 2 == 1)
            return vector<int>();
        if(int c = s.count(0))
        {
            for(int i=0; i<c>>1; i++)
                ret.push_back(0);
            s.erase(0);
        }
        while(! s.empty())
        {
            auto it = s.begin();
            ret.push_back(*it);
            auto doubleIt = s.find(*it << 1);
            if(doubleIt == s.end())
                return vector<int>();
            s.erase(it);
            s.erase(doubleIt);
        }
        return ret;
    }
};
