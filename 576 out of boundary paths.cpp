class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) 
    {
        long long ans = 0;
        // init
        vector<vector<vector<long long>>> tab(2, vector<vector<long long>>(m, vector<long long>(n, 0)));
        tab[0][startRow][startColumn] = 1LL;
        for(int move=0; move<maxMove; move++)
        {
            int move2 = move % 2; // filled in
            for(int col=0; col<n; col++)
            {
                ans += tab[move2][0][col];
                ans += tab[move2][m-1][col]; 
                ans %= 1000000007;
            }
            

            for(int row=0; row<m; row++)
            { 
                ans += tab[move2][row][0]; 
                ans += tab[move2][row][n-1]; 
                ans %= 1000000007;
            }
            
            int move1 = 1-move2;  // to be constructed
            for(int col=0; col<n; col++)
                for(int row=0; row<m; row++)
                {
                    long long sum = 0;
                    if(col != 0)
                        sum += tab[move2][row][col-1];
                    if(col != n-1)
                        sum += tab[move2][row][col+1];
                    if(row != 0)
                        sum += tab[move2][row-1][col];
                    if(row != m-1)
                        sum += tab[move2][row+1][col];
                    sum %= 1000000007;
                    tab[move1][row][col] += sum;
                }
            
            // init the other
            for(int col=0; col<n; col++)
                for(int row=0; row<m; row++)
                {
                    tab[move2][row][col] = 0LL;
                }
        }
        return ans;
    }
};
