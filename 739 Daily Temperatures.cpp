struct Elem
{
    int val;
    int idx;
    Elem(const int &val, const int &idx) : val(val), idx(idx) {}
};
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& t)
    {
        int n = t.size();
        stack<Elem> s;
        vector<int> ret(n);
        s.push(Elem(101, 0));
        for(int i = n-1; i>=0; i--)
        {
            while(s.top().val <= t[i])
                s.pop();
            if(s.top().val == 101)
                ret[i] = 0;
            else
                ret[i] = s.top().idx - i;
            s.push(Elem(t[i], i));
        }
        return ret;
    }
};
