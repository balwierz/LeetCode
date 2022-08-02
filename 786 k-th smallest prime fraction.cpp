class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k)
    {
        int n = arr.size();
        double l=0.0;  //1.0/arr[n-1];
        double r=1.0;
        double mid;
        //k--; // because input is 1-based;
        while(true)
        {
            int cnt = 0;
            mid = (l+r) / 2.0;
            for(int divI=1; divI<n; divI++)
            {
                int num = upper_bound(arr.begin(), arr.begin()+divI, arr[divI]*mid) -
                    arr.begin();
                cnt += num;
            }
            if(cnt == k)
                break;
            if(cnt < k)
                l = mid;
            else
                r = mid;
        }
        
        // now find this element:
        //cout << mid << endl;
        int i,j;
        double max = 0;
        for(int divI=1; divI<n; divI++)
        {
            int num = upper_bound(arr.begin(), arr.begin()+divI, arr[divI]*mid) -
                arr.begin();
            if(num)
            {
                double curr = (double)(arr[num-1]) / arr[divI];
                //cout << arr[num-1] << "/" << arr[divI] << endl;
                if(curr > max)
                {
                    max = curr;
                    i = num-1;
                    j = divI;
                }
            }
        }
        
        return vector<int> {arr[i], arr[j]};
    }
};
