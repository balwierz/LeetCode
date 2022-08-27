class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k)
    {
        int bestK = -1000000001;
        int m = matrix.size();
        int n = matrix[0].size();
        for(int L=0; L<n; L++)
        {
            vector<int> tab(m, 0);
            for(int R=L; R<n; R++)
            {
                // update cumsum(tab) L->R
                for(int i=0; i<m; i++)
                    tab[i] += matrix[i][R];
                int cs = 0;
                set<int> s;
                s.insert(0);
                for(int i=0; i<m; i++)
                {
                    cs += tab[i];
                    auto ub = s.lower_bound(cs - k);
                    if(ub != s.end())
                        bestK = max(bestK, cs - *ub);
                    if(bestK == k)
                        return k;
                    s.insert(cs);
                }
            }
        }
        return bestK;
    }
};
