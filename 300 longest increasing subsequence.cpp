class Solution {
    class Elem
    {
    public:
        Elem(const int &score, const int &value) : score(score), value(value) {}
        int score;
        int value;
        bool operator<(const Elem &other) const
        {
            //if(score == other.score)
            //    return value < other.value;
            return score > other.score; // it implements "greater"
        }
    };
public:
    int lengthOfLIS(vector<int>& nums)
    {
        set<Elem> s;
        for(int i=0; i<nums.size(); ++i)
        {
            //cout << "size " << s.size() << endl;
            auto it = s.begin();
            while(it != s.end())
            {
                //cout << "considering " << it->score << ' ' << it->value << endl;
                if(it->value < nums[i])
                {
                    // try if we have already an element with this score;
                    auto f = s.find(Elem(it->score+1, 0));
                    if(f != s.end())
                    {
                        if(nums[i] < f->value)
                        {
                            s.erase(f);
                            s.emplace((it->score)+1, nums[i]);
                        }
                    }
                    else
                    {
                        s.emplace((it->score)+1, nums[i]);
                    }
                    //cout << "emplacing " << it->score+1 << " " << nums[i] << endl;
                    goto foo;
                }
                it++;
            }
            {
                auto f = s.find(Elem(1, 0));
                if(f != s.end())
                {
                    if(nums[i] < f->value)
                    {
                        s.erase(f);
                        s.emplace(1, nums[i]);
                    }
                }
                else
                {
                    s.emplace(1, nums[i]);
                }
            }
            //cout << "de novo 1 " << nums[i] << endl;
            foo:
            1;
        }
        return s.begin()->score;
    }
    
    // quickest solution
    int lengthOfLIS2(vector<int>& nums) {
        vector<int> sub;
        for (int x : nums) {
            if (sub.empty() || sub[sub.size() - 1] < x) {
                sub.push_back(x);
            } else {
                auto it = lower_bound(sub.begin(), sub.end(), x); // Find the index of the smallest number >= x
                *it = x; // Replace that number with x
            }
        }
        return sub.size();
    }
};
