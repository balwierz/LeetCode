class Solution {
public:
    int kthSmallest(vector<vector<int>>& m, int k)
    {
        int n = m.size();
        int l = m[0][0], r = m[n-1][n-1];
        while(l<r)
        {
            int mid = (l + r) >> 1;
            int count = 0;
            for(int rowI = 0; rowI < n; rowI++)
            {
                count += upper_bound(m[rowI].begin(), m[rowI].end(), mid) -
                    m[rowI].begin();
            }
            if(count < k)
                l = mid+1;
            else
                r = mid;
        }
        return l;
    }
};
