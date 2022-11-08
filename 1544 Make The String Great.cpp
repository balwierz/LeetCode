class Solution {
    bool isBad(char a, char b)
    {
        //return abs(a-b) == 32; // or xor
        return (a ^ b) == 32;
    }
public:
    string makeGood(string s)
    {
        list<char> ll;
        for(char c : s)
            ll.push_back(c);
        bool didSth = true;
        while(didSth)
        {
            didSth = false;
            for(auto it2 = ll.begin(), it = it2++; it2 != ll.end(); it++, it2++)
            {
                while(isBad(*it, *it2))
                {
                    didSth = true;
                    auto tmp = it, tmp2 = it2;
                    bool isBegin = (it == ll.begin());
                    it--;
                    it2++;
                    ll.erase(tmp);
                    ll.erase(tmp2);
                    if(isBegin)
                        it = ll.begin();
                }
            }
        }
        string ret;
        for(auto it=ll.begin(); it != ll.end(); it++)
            ret.push_back(*it);
        return ret;
    }
};
