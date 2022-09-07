class E
{
    public:
    int val;
    int idx;
    bool operator<(const E &other)
    {
        return val < other.val;
    }
};
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int n = arr.size();
        if(n==0)
            return arr;
        vector<E> v(n);
        for(int i = 0; i<n; i++)
        {
            v[i].val=arr[i];
            v[i].idx=i;
        }
        sort(v.begin(), v.end());
        int rank = 1;
        int lastVal = v[0].val;
        arr[v[0].idx] = 1;
        for(int i=1; i<n; i++)
        {
            if(lastVal == v[i].val)
                arr[v[i].idx] = rank;
            else
            {
                arr[v[i].idx] = ++rank;
                lastVal = v[i].val;
            }
        }
        return arr;
    }
};
