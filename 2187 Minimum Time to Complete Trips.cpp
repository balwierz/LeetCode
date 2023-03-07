#pragma GCC optimize("Ofast","inline","-ffast-math")
#pragma GCC target("avx,mmx,sse2,sse3,sse4")
class Solution {
public:
    long long numTrips(long long time, vector<int>& tripTimes)
    {
        long long ret = 0;
        for(int &tripTime : tripTimes)
            ret += time / tripTime;
        return ret;
    }
    long long minimumTime(vector<int>& tripTimes, int totalTrips) 
    {
        ios::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        long long l = 0, r = (long long)totalTrips * *min_element(tripTimes.begin(), tripTimes.end());
        while(l + 1 < r)
        {
            long long mid = (l+r) / 2;
            if(numTrips(mid, tripTimes) < totalTrips)
                l = mid;
            else
                r = mid;
        }
        return r;
    }
};
