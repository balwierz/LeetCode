class Solution {
public:
    int trap(vector<int>& height)
    {
        int ret = 0;
        int n = height.size();
        int i = -1; // left and right iterators
        int j = n;
        int l=0;
        int r=0;  // barier heights
        while(i+1<j)
        {
            if(l<r)
            {
                i++;
                //cout << "i=" << i << endl;
                if(height[i] > l)
                    l = height[i];
                else
                    ret += l - height[i];
            }
            else
            {
                j--;
                //cout << "j=" << j << endl;
                if(height[j] > r)
                    r = height[j];
                else
                    ret += r - height[j];
            }
        }
        return ret;
    }
};
