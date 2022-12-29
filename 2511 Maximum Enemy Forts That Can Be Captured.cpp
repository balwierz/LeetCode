class Solution {
public:
    int captureForts(vector<int>& forts)
    {
        int start = forts[0];
        int bestLen = 0;
        int thisLen = 0;
        for(int c : forts)
        {
            if(c==0)
                thisLen++;
            else
            {
                if(start == -c)  // valid region
                    bestLen = max(bestLen, thisLen);
                thisLen = 0;
                start = c;
            }
        }
        return bestLen;
    }
};
