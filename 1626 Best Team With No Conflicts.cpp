class State
{
    public:
    int scoreThr;
    int csum;
    State(int t, int s) : scoreThr(t), csum(s) {}
};
class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) 
    {
        vector<vector<int>> data(1001, vector<int>());
        for(int i=0; i<scores.size(); i++)
            data[ages[i]].push_back(scores[i]);
        vector<State> ladder;  // decreasing order by threshold
        for(int a = 1000; a>0; a--)
        {
            if(data[a].size() == 0)
                continue;
            sort(data[a].begin(), data[a].end());
            auto dataIt = data[a].rbegin();
            auto ladderIt = ladder.begin();
            vector<State> newLadder;
            int maxLadder = 0;
            int maxData = 0;
            int runSum = 0;    // sums the scores at a give age in decreasing order
            while(dataIt != data[a].rend() || ladderIt != ladder.end())
            {
                int d = (dataIt != data[a].rend()) ? *dataIt : 0;
                int l = (ladderIt != ladder.end()) ? ladderIt->scoreThr : 0;
                if(l > d)
                {
                    newLadder.push_back(*ladderIt);
                    maxLadder = max(maxLadder, ladderIt++->csum);
                }
                else
                {
                    int ss = 0;
                    for(;dataIt != data[a].rend() && *dataIt == d; dataIt++)
                        ss += d;
                    maxData = ss + max(maxData, maxLadder);
                    if(d == l)
                        maxData = max(maxData, ss + ladderIt++->csum);
                    newLadder.emplace_back(d, maxData);
                }
            }
            ladder = newLadder;
        }
        int ret = 0;
        for(State& e : ladder)
        {
            if(e.csum > ret)
                ret = e.csum;
        }
        return ret;
    }
};
