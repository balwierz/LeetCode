#include <map>
#include <set>

vector<int> nm;
class Solution 
{
    struct subArr
    {
        int i, j; // [i,j)
        subArr(const int &_i, const int &_j) : i(_i), j(_j) {}
        bool operator< (const subArr &s) const
        {
            if(j-i != s.j-s.i)
                return j-i < s.j-s.i;
            for(int k=0; k<j-i;k++)
            {
                if(nm[i+k] != nm[s.i+k])
                    return nm[i+k] < nm[s.i+k];
            }
            return false; // they are equal
        }
    };
public:
    int countDistinct(vector<int>& nums, int k, int p) 
    {
        nm = nums;
        set<subArr> s;
        for(int i=0; i<nums.size(); i++)
        {
            int j=i;
            int m=0; // number of divisible numbers
            for(; j<nums.size(); j++)
            {
                if(nums[j] % p == 0)
                {
                    m++;
                    if(m > k)
                        break;
                }
                //cout << "i"<<i<< " j"<<j << " m"<<m << endl;
                s.emplace(i,j+1);
            }
        }
        //for(auto it=s.begin(); it!=s.end(); it++)
        //    cout << '(' << it->i << ',' << it->j << ") ";
        return s.size();
    }
};
