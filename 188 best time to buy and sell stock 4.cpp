struct interval
{
    int beg, end; // inclusive
    int bestBeg, bestEnd;
    int val;
    bool grow; // true grow
    bool operator<(const interval &other) const
    {
        return val < other.val;
    }
    interval(vector<int> &prices, int beg, int end, bool grow) : beg(beg), end(end), grow(grow) 
    {
        if(!grow)
            bestGrow(prices);
        else
            bestDrop(prices);
    }
    void bestGrow(vector<int>& prices)
    {
        int i=beg, j=beg;
        int best = 0, bestI=0, bestJ=0;
        while(j<=end)
        {
            int thisGain = prices[j] - prices[i];
            if(thisGain > best)
            {
                best = thisGain;
                bestI = i; bestJ = j;
            }
            else if(thisGain < 0)
            {
                i=j;
            }
            j++;
        }
        bestBeg = bestI;
        bestEnd = bestJ;
        val = best;
    }
    void bestDrop(vector<int>& prices)
    {
        int i=beg, j=beg;
        int best = 0, bestI=0, bestJ=0;
        while(j<=end)
        {
            int thisGain = - prices[j] + prices[i];
            if(thisGain > best)
            {
                best = thisGain;
                bestI = i; bestJ = j;
            }
            else if(thisGain < 0)
            {
                i=j;
            }
            j++;
        }
        bestBeg = bestI;
        bestEnd = bestJ;
        val = best;
    }
};


class Solution {

public:
    int maxProfit(int k, vector<int>& prices) 
    {
        int ret = 0;
        int n = prices.size();
        priority_queue<interval> q;
        interval full(prices, 0, n-1, false);
        q.push(full);
        for(int round = 0; round<k; round++)
        {
            interval best = q.top();
            q.pop();
            if(best.val == 0)
                return ret;
            ret += best.val;
            if(!best.grow)  // we have a best growing subinterval
            {
                if(best.beg +1 < best.bestBeg)
                {
                    interval left(prices, best.beg, best.bestBeg-1, false);
                    q.push(left);
                }
                interval central(prices, best.bestBeg, best.bestEnd, true);
                q.push(central);
                if(best.bestEnd + 1 < best.end)
                {
                    interval right(prices, best.bestEnd+1, best.end, false);
                    q.push(right);
                }
            }
            else // we have a best dropping subinterval within a growing
            {
                if(best.beg +1 < best.bestBeg)
                {
                    interval left(prices, best.beg, best.bestBeg-1, true);
                    q.push(left);
                }
                interval central(prices, best.bestBeg, best.bestEnd, false);
                q.push(central);
                if(best.bestEnd + 1 < best.end)
                {
                    interval right(prices, best.bestEnd+1, best.end, true);
                    q.push(right);
                }
            }
        }
        return ret;
    }
};
