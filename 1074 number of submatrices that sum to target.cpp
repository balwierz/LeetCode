class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target)
    {
        int m = matrix.size();
        int n = matrix[0].size();
        int cumsum[m+1][n+1];
        memset(cumsum, 0, sizeof(cumsum));
        for(int i=1; i<=m; i++)
        {
            for(int j=1; j<=n; j++)
            {
                cumsum[i][j] = matrix[i-1][j-1] + cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1];
                //cout << i << " " << j << " " << cumsum[i][j] << endl;
            }
        }
        
        int ret = 0;
        for(int row1=1; row1<=m; row1++)
            for(int row2=row1; row2<=m; row2++)
            {
                cout << row1 << " to " << row2 << endl;
                unordered_multimap<int, int> sum2ind; // index is 1d cumsum, value is column number
                int tab[n+1];  // 1d cumsum
                for(int col=0; col<=n; col++)
                {
                    int sum = cumsum[row2][col] - cumsum[row1-1][col];
                    sum2ind.insert(make_pair(sum, col));
                    tab[col] = sum;
                    //cout << sum << endl;
                }
                // now we go over all the elements of tab and seach for the correct values in hash
                // and check if the corresponding index is >= of the current index
                for(int col=0; col<=n; col++)
                {
                    auto its = sum2ind.equal_range(tab[col] + target);
                    for(auto it=its.first; it!=its.second; it++)
                        if(it->second > col)
                        {
                            //cout << "found " << col << " " << it->second << endl;
                            ret++;
                        }
                }
            }
        return ret;
    }
};
