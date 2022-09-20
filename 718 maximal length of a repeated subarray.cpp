 
// custom specialization of std::hash can be injected in namespace std
template<>
struct std::hash<pair<int,int>>
{
    std::size_t operator()(pair<int,int> const& s) const noexcept
    {
        std::size_t h1 = std::hash<int>{}(s.first);
        std::size_t h2 = std::hash<int>{}(s.second);
        return h1 ^ (h2 << 1); // or use boost::hash_combine
    }
};

class Solution2
{
public:
    int findLength(vector<int>& nums1, vector<int>& nums2)
    {
        vector<vector<int>> int2positions(102);
        unordered_set<pair<int,int>> subarrays;  // start and ending position
        int ret = 0;
        // preprocess the longer array (not sure)
        if(nums1.size() < nums2.size())
            swap(nums1, nums2);
        for(int i=0; i<nums1.size(); i++)
        {
            int2positions[nums1[i]].push_back(i);
        }
        nums2.push_back(101); // sentinel to terminate all the current arrays in the end.
        // build a set of subarrays
        //cout << "main loop\n";
        vector<bool> isEnd(nums1.size(), false);
        for(int num : nums2)
        {
            //cout << num << endl;
            unordered_set<pair<int,int>> newSubarrays;
            // extend existing first:
            for(const pair<int,int> &subarray : subarrays)
            {
                
                if(subarray.second + 1 == nums1.size() ||
                   nums1[subarray.second + 1] != num)
                {
                    // end the current array:
                    ret = max(ret, subarray.second - subarray.first + 1);
                    isEnd[subarray.second] = false;
                }
                else
                {
                    //cout << "[" << subarray.first << ", " << subarray.second + 1 << "]" << endl;
                    newSubarrays.emplace(subarray.first, subarray.second + 1);
                    isEnd[subarray.second + 1] = true;
                    isEnd[subarray.second] = false;
                }
            }
            // start new subarrays at all ocurrences of num in nums1:
            //cout << "start new\n";
            for(int position : int2positions[num])
            {
                if(!isEnd[position])
                {
                    //cout << "  *[" << position << ", " << position << "]" << endl;
                    newSubarrays.emplace(position, position);
                    isEnd[position] = true;
                }
            }
            // loop end condition
            subarrays = newSubarrays;  // I wonder what's the complexity of this.
        }
        return ret;
    }
};

class Solution
{
public:
    int findLength(vector<int>& nums1, vector<int>& nums2)
    {
        int ret = 0;
        vector<vector<int>> memo(nums2.size() + 1, vector<int>(nums1.size()+1, 0));
        for(int i=nums1.size()-1; i>=0; i--)
            for(int j=nums2.size()-1; j>=0; j--)
                if(nums1[i] == nums2[j])
                    memo[j][i] = memo[j+1][i+1] + 1;
        cout << "checking" << endl;
        for(int i=0; i<nums2.size(); i++)
            ret = max(ret, accumulate(memo[i].begin(), memo[i].end(), INT_MIN,
                                      [](const int &a, const int &b)
                                      {
                                          return max(a, b);
                                      }));
        return ret;
    }
};
