class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) 
    {
        priority_queue<int> q(gifts.begin(), gifts.end());
        for(int i=0; i<k; i++)
        {
            int num = q.top();
            q.pop();
            q.push((int)sqrt(num));
        }
        long long ret = 0;
        while(! q.empty())
        {
            ret += q.top();
            q.pop();
        }
        return ret;
    }
};
