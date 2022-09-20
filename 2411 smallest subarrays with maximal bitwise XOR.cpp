class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums)
    {
        vector<int> lastSet(30, -1);
        multiset<int> ends;
        vector <int> ret;
        for(int i=nums.size()-1; i>=0; i--)
        {
            //cout << "i=" << i << endl;
            for(int bit=0; bit<30; bit++)
                if((nums[i]>>bit) & 1)  // bit bit is set
                {
                    //cout << "bit=" << bit << " ";
                    if(lastSet[bit] != -1)
                    {
                        auto elem = ends.find(lastSet[bit]);
                        ends.erase(elem);
                    }
                    lastSet[bit] = i;
                    ends.insert(i);
                }
            auto it = ends.rbegin();
            if(it != ends.rend())
            {
                int minLenForMaxBitmask = *it;
                ret.push_back(minLenForMaxBitmask-i +1);
            }
            else
            {
                ret.push_back(1);
            }
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
