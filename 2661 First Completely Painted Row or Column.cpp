class Solution {
public:
    Solution()
    {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
    }
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat)
    {
        int m = mat.size();
        int n = mat[0].size();
        vector<int> rowRemain(m, n);
        vector<int> colRemain(n, m);
        vector<pair<int,int>> num2coords(m*n+1);
        for(int row = 0; row<m; row++)
            for(int col = 0; col<n; col++)
                num2coords[mat[row][col]] = make_pair(row, col);
        int ret = 0;
        for(int num : arr)
        {
            rowRemain[num2coords[num].first] --;
            if(rowRemain[num2coords[num].first] == 0)
                return ret;
            colRemain[num2coords[num].second] --;
            if(colRemain[num2coords[num].second] == 0)
                return ret;
            ret ++;
        }
        return 0; // never happens
    }
};
