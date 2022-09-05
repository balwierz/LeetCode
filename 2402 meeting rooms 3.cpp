class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings)
    {
        sort(meetings.begin(), meetings.end(), [](vector<int> &a, vector<int> &b) {return a[0] < b[0];});
        vector<int> bookNum(n, 0);
        set<int> freeRooms;
        for(int i =0; i<n; i++)
            freeRooms.insert(i);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> meetingEnds;  // keys {endTime, roomNum}
        int meetingI = 0;
        long long time = 0;
        while(meetingI < meetings.size())
        {
            long long nextMeetingEnd = INT_MAX;
            if(! meetingEnds.empty())
                nextMeetingEnd = meetingEnds.top().first;
            long long nextMeetingStart = meetings[meetingI][0];
            while(nextMeetingEnd <= nextMeetingStart || freeRooms.empty())
            {
                //cout << "ending room=" << meetingEnds.top().second << " when=" << meetingEnds.top().first << endl;
                freeRooms.insert(meetingEnds.top().second);
                meetingEnds.pop();
                time = nextMeetingEnd;
                nextMeetingEnd = INT_MAX;
                if(! meetingEnds.empty())
                    nextMeetingEnd = meetingEnds.top().first;
                
            }
            while(! freeRooms.empty() && nextMeetingStart < nextMeetingEnd && meetingI < meetings.size())
            {
                long long when = max(time, nextMeetingStart);
                int duration = meetings[meetingI][1] - meetings[meetingI][0];
                int where = *freeRooms.begin();
                // schedule:
                //cout << "starting room=" << where << " when=" << when << endl;
                bookNum[where]++;
                meetingEnds.push({when+duration, where});
                freeRooms.erase(where);
                meetingI++;
                time = when;
                if(meetingI < meetings.size())
                    nextMeetingStart = meetings[meetingI][0]; //max(when, (long long));
                else
                    nextMeetingStart = INT_MAX;
                nextMeetingEnd = INT_MAX;
                if(! meetingEnds.empty())
                    nextMeetingEnd = meetingEnds.top().first;
            }
        }
        int ret = 0;
        for(int i=0; i<n; i++)
        {
            //cout << bookNum[i] << " ";
            if(bookNum[i] > bookNum[ret])
            {
                ret = i;
            }
        }
        return ret;
    }
};
