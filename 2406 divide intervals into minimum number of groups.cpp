class Solution {
public:
    int minGroups(vector<vector<int>>& intervals)
    {
        int ret = 0;
        sort(intervals.begin(), intervals.end(), 
             [](vector<int> &a, vector<int> &b) {return a[0] < b[0];});
        priority_queue<int, vector<int>, greater<int>> ends;
        
        for(auto it = intervals.begin(); it != intervals.end(); it++)    
        {
            while(! ends.empty() && ends.top() < (*it)[0]) //
                ends.pop();
            ends.push((*it)[1]);
            ret = max(ret, (int)ends.size());
        }
        return ret;
    }
    int minGroups2(vector<vector<int>>& intervals)
    {
        int ret = 0;
        sort(intervals.begin(), intervals.end(), 
             [](vector<int> &a, vector<int> &b) {return a[0] < b[0];});
        list<vector<int>> ll(intervals.begin(), intervals.end());
        while(! ll.empty())
        {
            int tail = -1;
            auto it = ll.begin();
            ret ++;
            while(it != ll.end())
            {
                while(it != ll.end() && (*it)[0] <= tail)
                    it++;
                if(it == ll.end())
                    break;
                tail = (*it)[1];
                auto nextIt = it; nextIt++;
                ll.erase(it);
                it = nextIt;
            }
            
        }
        return ret;
    }
};
