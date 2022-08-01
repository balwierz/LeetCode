class Solution {
public:
    int longestCycle(vector<int>& edges)
    {
        int ret = -1;
        int n = edges.size();
        vector<int> seen(n, -1);
        vector<int> depth(n, 0);
        for(int i=0; i<n; i++)
        {
            int cur = i;
            int d = 0;
            while(seen[cur] == -1)
            {
                seen[cur] = i;
                depth[cur] = d++;
                cur = edges[cur];
                if(cur == -1)
                    break;
            }
            if(cur == -1)
                continue;
            if(seen[cur] == i)   // same round
            {
                int curDepth = d-depth[cur];
                if(curDepth > ret)
                    ret = curDepth;
            } // else nop
        }
        return ret;
    }
};
