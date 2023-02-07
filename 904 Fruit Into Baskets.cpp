class Solution {
public:
    int totalFruit(vector<int>& fruits)
    {
        unordered_map<int, int> counts;
        int ret = 0;
        int cur = 0;
        int j=0;   // next index to remove
        for(int f : fruits)
        {
            while(counts.size() == 2 && counts.count(f) == 0)
            {
                cur --;
                counts[fruits[j]] --;
                if(counts[fruits[j]] == 0)
                    counts.erase(fruits[j]);
                j++;
            }
            counts[f] ++;
            cur ++;
            ret = max(ret, cur);
        }
        return ret;
    }
};
