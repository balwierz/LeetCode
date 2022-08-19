class Solution {
public:
    bool isPossible(vector<int>& nums)
    {
        priority_queue<int> begs;
        int i = 0;
        int lastVal = nums[0]-1;
        int lastN = 0;
        nums.push_back(nums[nums.size()-1] + 2);
        while(i<nums.size())
        {
            // cout the number of identical values, i needs to point to the first one 
            int n = 0;
            int thisVal = nums[i];
            bool fGap = (thisVal > lastVal + 1);
            int start = nums[i];
            if(! fGap)
                while(i<nums.size() && nums[i] == lastVal + 1)
                {
                    i++; n++;
                }
            //cout << "start=" << start << " thisVal=" << thisVal << " n=" << n << endl;
            
            int delta = n - lastN;
            if(fGap)
            {
                // there is a gap
                delta = -lastN;
                thisVal = lastVal + 1;
                n = 0;
            }
            while(delta > 0)
            {
                // open new ranges
                begs.push(-start);
                delta--;
                cout << " starting " << start << endl;
            }
            while(delta < 0)
            {
                // try finishing the longest ranges
                int beg = - begs.top();
                begs.pop();
                delta++;
                cout << " finishing " << beg << " thisVal" << thisVal << endl;
                if(thisVal - beg < 3)
                    return false;
            }
            lastVal = thisVal;
            lastN = n;
        }
        return true;
    }
};
