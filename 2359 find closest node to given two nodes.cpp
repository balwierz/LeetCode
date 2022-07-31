class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2)
    {
        vector<int> d1(edges.size(), 999999);
        vector<int> d2(edges.size(), 999999);
        int n = node1;
        //d1[node1] = 0;
        int cntr = 0;
        while(d1[n] == 999999)
        {
            d1[n] = cntr++;
            if(edges[n] == -1)
                break;
            n = edges[n];
        }
        //d2[node2] = 0;
        n = node2;
        cntr = 0;
        while(d2[n] == 999999)
        {
            d2[n] = cntr++;
            if(edges[n] == -1)
                break;
            n = edges[n];
        }
        int bestNode = -1;
        int bestDist = 999999;
        for(int i=0; i<edges.size(); ++i)
        {
            int m = max(d1[i], d2[i]);
            if(m < bestDist)
            {
                bestDist = m;
                bestNode = i;
            }
        }
        return bestNode;
    }
};
