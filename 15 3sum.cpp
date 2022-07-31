#include <unordered_set>

class Solution {
    struct triple
    {
        vector<int> x;
        bool operator==(const triple& other) const
        {
            return x[0] == other.x[0] && x[1] == other.x[1] && x[2] == other.x[2];
        }
        /*bool operator<(const triple& other)
        {
            if(x[0]<other[0])
                return true;
            if(x[1]<other[1])
                return true;
            if(x[2]<other[2])
                return true;
            return false;
        }*/
        triple() : x(3)
        {
        }
        triple(vector<int> a) : x(a.begin(), a.end())
        {
            sort(x.begin(), x.end());
        }
        operator vector<int>() const
        {
            return x;
        }
        int operator[] (const int &i) const
        {
            return x[i];
        }
    };
    struct tripleHash 
    {
        size_t operator()(const triple& v) const 
        {
        std::hash<int> hasher;
        size_t seed = 0;
        for (int i : v.x) 
        {
            seed ^= hasher(i) + 0x9e3779b9 + (seed<<6) + (seed>>2);
        }
        return seed;
        }
    };
public:
    vector<vector<int>> threeSum(vector<int>& nums)
    {
        unordered_map<int, int> tmp;
        for(int n:nums)
            tmp[n]++;
        nums = {};
        for(auto &it:tmp)
        {
            nums.push_back(it.first);
            if(it.second > 1)
                nums.push_back(it.first);
            if(it.second > 2)
                nums.push_back(it.first);
        }
        
        unordered_set<triple, tripleHash> ret;
        sort(nums.begin(), nums.end());
        for(int i=0; i<nums.size()-2; i++)
        {
            int j=i+1, k=nums.size()-1;
            while(j<k)
            {
                int sum = nums[i] + nums[j] + nums[k];
                if(sum == 0)
                    ret.emplace(vector<int>{nums[i], nums[j], nums[k]});
                if(sum < 0)
                    j++;
                else
                    k--;
            }
        }
        vector<vector<int>> ret2(ret.begin(), ret.end());
        return(ret2);
    }
    vector<vector<int>> threeSum_bak(vector<int>& nums) 
    {
        if(nums.size() < 3)
            return(vector<vector<int>>());
        unordered_multiset<int> nn(nums.begin(), nums.end());
        //cout << nn.size() << endl;
        //sort(nums.begin(), nums.end());
        unordered_set<triple, tripleHash> ret;
        for(int i = 0; i<nums.size()-2; i++)
        {
            int a = nums[i];
            auto ita = nn.find(a);
            nn.erase(ita);
            //cout << "foo" << i << endl;
            //cout << nn.size() << endl;
            for(int j=i+1; j<nums.size()-1; j++)
            {
                int b = nums[j];
                auto itb = nn.find(b);
                nn.erase(itb);
                //cout << "bar" << j << endl;
                //cout << nn.size() << endl;
                auto it = nn.find(-a -b);
                if(it != nn.end())
                {
                    //cout << "found" << endl;
                    ret.emplace(vector<int>({a, b, -a -b}));
                }
                nn.insert(b);
            }
            //nn.insert(a);
        }
        vector<vector<int>> ret2(ret.begin(), ret.end());
        return(ret2);
    }
};
