#include <map>
class Solution {
public:
    int minimumCardPickup(vector<int>& cards) 
    {
        int minCards = 999999;
        unordered_map<int, int> lastPos;
        for(int i=0; i<cards.size(); i++)
        {
            int c = cards[i];
            if(lastPos.find(c) != lastPos.end())
            {
                int thisDist = i-lastPos[c];
                if(thisDist == 1)
                    return 2;
                if(thisDist < minCards)
                    minCards = thisDist;
                lastPos[c] = i;
            }
            lastPos[c] = i;
        }
        if(minCards != 999999)
            return minCards+1;
        else
            return -1;
    }
};
