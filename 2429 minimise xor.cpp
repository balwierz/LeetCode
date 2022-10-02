    int minimizeXor(int num1, int num2) 
    {
        int nBit = __builtin_popcount(num2);
        int ret = 0;
        set<int> unset;
        for(int i=31; nBit && i>=0; i--)
        {
            if((num1 >> i) & 1)
            {
                ret |= (1 << i);
                nBit--;
            }
            else
                unset.insert(i);
        }
        while(nBit--)
        {
            auto w = unset.begin();
            ret |= (1 << *w);
            unset.erase(w);
        }
        return ret;
    }
