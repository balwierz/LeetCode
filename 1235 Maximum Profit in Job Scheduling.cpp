class Task
{
    public:
    int start, end, profit;
    bool operator<(const Task &other) const
    {
        return end < other.end;
    }
};
class Solution {
public:
    int jobScheduling(vector<int>& start, vector<int>& end, vector<int>& profit)
    {
        int n = start.size();
        vector<Task> tasks(n);
        for(int i=0; i<n; i++)
        {
            tasks[i].start = start[i]; tasks[i].end = end[i]; tasks[i].profit = profit[i];
        }
        sort(tasks.begin(), tasks.end());
        map<int, int> end2prof;
        end2prof[0] = 0;
        for(int i=0; i<n; i++)
        {
            int e = tasks[i].end;
            int currBest = end2prof.rbegin()->second; // current best estimate without adding new elem
            while(i<n && tasks[i].end == e)
            {
                auto it = end2prof.lower_bound(tasks[i].start);
                if(it == end2prof.end() || it->first > tasks[i].start)
                    it--;
                int tmp = it->second + tasks[i].profit;
                currBest = max(currBest, tmp);
                i++;
            }
            i--;
            end2prof[e] = currBest;
        }
        return end2prof.rbegin()->second;
    }
};
