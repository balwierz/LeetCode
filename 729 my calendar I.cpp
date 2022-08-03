class MyCalendar {
    struct interval
    {
        int l, r;
        bool operator<(const interval &other) const
            return(other.r<=l);
        interval(int a, int b) : l(a), r(b) {}
    };
    set<interval> mp;
public:
    bool book(int start, int end)
    {
        interval a(start, end);
        if(! mp.count(a))
        {
            mp.insert(a);
            return true;
        }
        return false;
    }
};
