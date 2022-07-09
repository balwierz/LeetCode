#include <queue>

struct Elem
{
    int val;
    int ind;
    Elem() {}
    Elem(const int &v, const int &i) : val(v), ind(i) {}
    bool operator<(const Elem &s) const
    {
        return val < s.val;
    }
};

class Solution 
{
public:
    int maxResult(vector<int>& nums, int k) 
    {
        int n = nums.size();
        priority_queue<Elem> prio;
        prio.emplace(nums[0], 0);
        for(int i=1; i<n; i++)
        {
            Elem bestElem;
            while(true)
            {
                bestElem = prio.top();
                if(bestElem.ind + k < i)
                {
                    prio.pop();
                    //cout << "Removing " << bestElem.ind << " " << bestElem.val << endl;
                }
                else
                    break;
            }
            // new element
            if(i == n-1)
            {
                return(bestElem.val + nums[i]);
            }
            prio.emplace(bestElem.val + nums[i], i);
            //cout << "inserting " <<  i << ' ' << bestElem.val + nums[i] << endl;
        }
        return(nums[0]); // will only be used when length=1;
    }
};
