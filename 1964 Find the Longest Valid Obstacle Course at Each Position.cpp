template<class a, class b, class c> ostream &operator<<(ostream &os, const map<a,b, c> &m)
{
    os << "map:";
    for(const auto &[k, v]: m)
        os << " " << k << ":" << v;
    return os;
}

class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles)
    {
        vector<int> ret;
        ret.reserve(obstacles.size());
        map<int, int, std::greater<int>> last2len;
        for(int o : obstacles)
        {
            //cout << "got " << o << endl;
            //cout << last2len << endl;
            auto it = last2len.lower_bound(o);
            int thisLen = 1;
            if(it != last2len.end())
            {
                thisLen = it->second + 1;
            }
            ret.push_back(thisLen);
            last2len[o] = thisLen;
            // invalidate all smaller or equal values to the left
            it = last2len.find(o);
            if(it == last2len.begin())
                continue;
            it--;
            while(true)
            {
                if(it == last2len.begin())
                {
                    if(it->second <= thisLen)
                        last2len.erase(it);
                    break;
                }
                if(it->second <= thisLen)
                {
                    auto toDel = it;
                    it--;
                    last2len.erase(toDel);
                }
                else
                    break;   
            }

        }
        return ret;
    }
};
