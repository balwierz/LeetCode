class Solution {
public:
    int minStoneSum(vector<int>& piles, int k)
    {
        int sum = 0;
        priority_queue<int> q;
        for(int p : piles)
        {
            q.push(p);
            sum += p;
        }
        for(int i=0; i<k; i++)
        {
            int val = q.top();
            q.pop();
            int o = val >> 1;
            sum -= o;
            q.push(val-o);
        }
        return sum;
    }
};
