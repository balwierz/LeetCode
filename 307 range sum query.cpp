class NumArray {
    vector<int> bit;
    vector<int> arr;
public:
    NumArray(vector<int>& nums)
    {  // construct BIT
        arr = nums;
        bit = vector<int>(nums.size()+1);
        bit[0] = 0;
        for(int i=0; i<nums.size(); ++i)
        {
            int k=i+1;
            while(k < bit.size())
            {
                bit[k] += nums[i];
                k += k & (-k);
            }
        }
    }
    
    void update(int index, int val)
    {
        int delta = val - arr[index];
        arr[index] = val;
        int k=index+1;
        while(k < bit.size())
        {
            bit[k] += delta;
            k += k & (-k);
        }
    }
    
    int cumSum(int i)  // including the number.
    {
        int ret = 0;
        int k=i+1;
        while(k)
        {
            ret += bit[k];
            k -= k & (-k);
        }
        return ret;
    }
    
    int sumRange(int left, int right)
    {
        return cumSum(right) - cumSum(left-1);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
