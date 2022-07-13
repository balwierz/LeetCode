class Solution {
public:
    int numTrees(int n)
    {
        int v[20];
        v[0] = 1;
        v[1] = 1;
        for(int i=2; i<=n; i++)
        {
            v[i] = 0;
            for(int j=0; j<i; j++)
            {
                v[i] += v[j]*v[i-j-1];
            }
        }
        return v[n];
    }
};
