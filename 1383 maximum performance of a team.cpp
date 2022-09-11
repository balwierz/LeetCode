class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k)
    {
        vector<pair<int,int>> workers(n);
        for(int i = 0; i<n; i++)
            workers[i] = {efficiency[i], speed[i]};
        sort(workers.rbegin(), workers.rend());
        priority_queue<int, vector<int>, greater<int>> pq;
        long long ret = 0;
        long long sumSpeed = 0;
        for(auto& [eff, speed] : workers)
        {
            pq.push(speed);
            sumSpeed += speed;
            if(pq.size() > k)
            {
                sumSpeed -= pq.top();
                pq.pop();
            }
            ret = max(ret, eff * sumSpeed);
        }
        return ret % ((int)1e9+7);
    }
};
