class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat)
    {
        int m = mat.size();
        int n = mat[0].size();
        for(int row=m-2; row>0; row--)
        {
            vector<int> tmp;
            int j=0; int i=row;
            while(i<m && j<n)
                tmp.push_back(mat[i++][j++]);
            sort(tmp.begin(), tmp.end());
            j=0; i=row; int w = 0;
            while(w<tmp.size())
                mat[i++][j++] = tmp[w++];
        }
        for(int col=0; col<n-1; col++)
        {
            vector<int> tmp;
            int i=0; int j=col;
            while(i<m && j<n)
                tmp.push_back(mat[i++][j++]);
            sort(tmp.begin(), tmp.end());
            i = 0; j=col; int w = 0;
            while(w < tmp.size())
                mat[i++][j++] = tmp[w++];
        }
        return mat;
    }
};
