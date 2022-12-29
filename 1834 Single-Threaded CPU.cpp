struct Task
{
    int enq;
    int runTime;
    int index;
    bool operator<(const Task &other) const
    {
        if(runTime == other.runTime)
            return index < other.index;
        return runTime < other.runTime;
    }
    bool operator>(const Task &other) const
    {
        if(runTime == other.runTime)
            return index > other.index;
        return runTime > other.runTime;
    }
    Task() {}    
    Task(int enq, int runTime, int index) : enq(enq), runTime(runTime), index(index) {}
};
class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) 
    {
        int n = tasks.size();
        priority_queue<Task, vector<Task>, greater<Task>> prio;
        vector<Task> tasks2(n);
        for(int i = 0; i<n; i++)
            tasks2[i] = Task(tasks[i][0], tasks[i][1], i);
        // sort tasks by start position
        sort(tasks2.begin(), tasks2.end(), 
            [](const Task &a, const Task &b) {return a.enq < b.enq;});
        long long time = tasks2[0].enq;
        vector<int> ret;
        // time points to the time of the finish of finishing task
        // We need to add new tasks that start at <= time
        int nextTaskI = 0;
        while(true)
        {
            while(nextTaskI < n && tasks2[nextTaskI].enq <= time)
            {
                prio.push(tasks2[nextTaskI]);
                nextTaskI ++;
            }
            // choose the next task from the priority queue
            if(prio.size())
            {
                time += prio.top().runTime;
                ret.push_back(prio.top().index);
                prio.pop();
            }
            else
            {
                if(nextTaskI == n)
                    break;
                time = tasks2[nextTaskI].enq;
            }
        }
        return ret;
    }
};
