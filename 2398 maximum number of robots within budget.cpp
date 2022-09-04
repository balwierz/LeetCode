class Solution {
public:
    long long cost(const set<int> &win, const int &k, const long long &winSum )
    {
        if(win.empty())
            return 0;
        return *(win.rbegin()) + k * winSum;
    }
    int maximumRobots(vector<int>& chargeTimes, vector<int>& runningCosts, long long budget)
    {
        int n = chargeTimes.size();
        long long winSum = 0;
        set<int> win;
        int i=0, j=0;
        int ret = 0;
        while(j < n)
        {
            while(j <= n && cost(win, j-i, winSum) <= budget)
            {
                //cout << "j " << j << endl;
                ret = max(ret, j-i);
                if(j < n)
                {
                    win.insert(chargeTimes[j]);
                    winSum += runningCosts[j];
                }
                j++;
            }
            while(cost(win, j-i, winSum) > budget)
            {
                //cout << "i " << i << endl;
                win.erase(chargeTimes[i]);
                winSum -= runningCosts[i];
                i++;
            }
        }
        return ret;
    }
};
