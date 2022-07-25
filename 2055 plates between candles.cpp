class Solution {
public:
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) 
    {
        s += "|";   // guardian
        int n = s.size();
        vector<int> cumsum(n);
        vector<int> rightCandle(n);
        int sum = 0;
        int smallSum = 0;
        int i=0;
        for(; i<n; i++)
        {
            cumsum[i] = 0;
            if(s[i] == '|')
                break;
        }
        for(; i<n; i++)
        {
            if(s[i] == '*')
            {
                smallSum++;
                cumsum[i] = sum; // no update
            }
            else  // "|"
            {
                cumsum[i] = sum = sum + smallSum;
                smallSum = 0;
            }
        }
        // right candle
        int lastCandle = n-1;
        i = n-2;
        for(; i>=0; i--)
        {
            if(s[i] == '*')
            {
                rightCandle[i] = lastCandle;
            }
            else
            {
                rightCandle[i] = i;
                lastCandle = i;
            }
        }
        // process queries
        vector<int> ret(queries.size());
        for(int q=0; q<queries.size(); ++q)
        {
            if(cumsum[queries[q][0]] == cumsum[queries[q][1]])
                ret[q] = 0;
            else
            {
                int a = cumsum[queries[q][1]];
                int b = cumsum[rightCandle[queries[q][0]]];
                ret[q] = a-b;
            }
        }
        return ret;
    }
};
