struct Event
{
    int time;
    char type;
    Event(int time, char type) : time(time), type(type) {  }
    bool operator<(const Event &other) const
    {
        if(time == other.time)
            return type < other.type;
        return time < other.time;
    }
};
class MyCalendarThree {
    multiset<Event> events;
public:
    MyCalendarThree() { }
    int book(int start, int end)
    {
        events.emplace(start, 's');
        events.emplace(end, 'e');
        int maxOverlap = 0;
        int curOverlap = 0;
        for(const auto &ev : events)  // ordered by time, and ends being earlier than starts
        {
            if(ev.type == 'e')
            {
                curOverlap --;
            }
            else // 's' start
            {
                curOverlap ++;
                maxOverlap = max(maxOverlap, curOverlap);
            }
        }
        return maxOverlap;
    }
};
