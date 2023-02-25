template < class T >
std::ostream& operator << (std::ostream& os, const std::vector<T>& v) 
{
    os << "[";
    for (typename std::vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        os << " " << *ii;
    }
    os << "]";
    return os;
}

template < class T >
std::ostream& operator << (std::ostream& os, const std::multiset<T>& v) 
{
    os << "[";
    for (typename std::multiset<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        os << " " << *ii;
    }
    os << "]";
    return os;
}

struct Elem
{
    int val;
    int maxVal;
    Elem(int val, int maxVal) : val(val), maxVal(maxVal) {}
    bool operator<(const Elem &other) const
    {
        return val < other.val;
    }
};


ostream& operator<<(ostream& os, const Elem& e)
{
    os << e.val << " {" << e.maxVal << "}";
    return os;
}

 
class Solution3
{
public:
    int minimumDeviation(vector<int>& nums) 
    {
        set<int> s;
        for(int num: nums) 
        {
            // insert max num
            if(num % 2 == 1) num *= 2;
            s.insert(num); 
        }
        
        int answer = *s.rbegin() - *s.begin();
        while(*s.rbegin() % 2 == 0) 
        {
            int num = *s.rbegin();
            s.erase(num);
            s.insert(num/2);
            answer = min(answer, *s.rbegin() - *s.begin());
        }
        return answer;
    }
};

class Solution 
{
public:
    int minimumDeviation(vector<int>& nums) 
    {
        vector<Elem> elem;
        for(int x : nums)
        {
            if(x % 2)  // odd
                elem.emplace_back(x, x<<1);
            else
            {
                int m = x;
                while((m & 1) == 0)
                    m >>= 1;
                elem.emplace_back(m, x);
            }
        }
        int ret = INT_MAX;
        multiset<Elem> data(elem.begin(), elem.end());
        while(true)
        {
            auto it = data.begin();
            int val = it->val;
            int maxVal = it->maxVal;
            ret = min(ret, data.rbegin()->val - val);
            if(val == maxVal)
                break;
            data.erase(it);
            data.emplace(val << 1, maxVal);
        }
        return ret;
    }
};
