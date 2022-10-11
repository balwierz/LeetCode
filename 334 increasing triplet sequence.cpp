class Solution {
public:
    bool increasingTriplet(vector<int>& nums)
    {
        int minVal = INT_MAX, twoVal = INT_MAX;
        for(int num : nums)
        {
            if(num > twoVal) return true;
            if(num < minVal) minVal = num;
            else if(minVal < num) twoVal = num;
        }
        return false;
    }
};
