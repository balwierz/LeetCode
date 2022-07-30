class Solution {
public:
    int shortestSequence(vector<int>& rolls, int k) 
    {
        int ret = 1;
        unordered_set<int> seen;
        int nSeen = 0;
        for(int &a:rolls)
            if(!seen.count(a))
            {
                if(++nSeen == k)
                {
                    seen.clear();
                    nSeen = 0;
                    ret++;
                }
                else
                    seen.insert(a);
            }
        return ret;
    }
};
