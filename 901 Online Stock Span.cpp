class StockSpanner
{
    stack<pair<int, int>, vector<pair<int,int>>> s;
    int n;
public:
    StockSpanner()
    {
        n = 0;
        s.push({INT_MAX, 0});
    }
    
    int next(int price) 
    {
        while(s.top().first <= price)
            s.pop();
        int ret = ++n - s.top().second;
        s.push({price, n});
        return ret;
    }
};
