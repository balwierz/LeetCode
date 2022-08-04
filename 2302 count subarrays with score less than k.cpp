static auto speedup = []() {
    ios_base::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);
    return NULL;
}();

class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k)
    {
        long long ret = 0;
        int i = 0;
        int j = 0;
        long long sum = 0;
        int n = nums.size();
        while(j<n)
        {
            sum += nums[j++];
            while(sum * (j-i) >= k)
            {
                sum -= nums[i++];
            }
            ret += (j-i);
            //cout << i << ' ' << j << " " << (j-i) << endl;
        }
        return ret;
    }
};
