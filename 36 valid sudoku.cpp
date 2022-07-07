#include <set>
class Solution {
    multiset<char> ms;
    bool validateSet()
    {
        for(char i : {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
        {
            if(ms.count(i) > 1)
                return false;
        }
        return true;
    }
public:
    bool isValidSudoku(vector<vector<char>>& board) 
    {
        // rows
        for(int r=0; r<9; r++)
        {
            for(int c=0; c<9; c++)
                ms.insert(board[r][c]);
            if(! validateSet())
                return false;
            ms.clear();
        }

        // columns
        cout << "columns\n";
        for(int c=0; c<9; c++)
        {
            for(int r=0; r<9; r++)
            {
                ms.insert(board[r][c]);
            }
            if(! validateSet())
                return false;
            ms.clear();
        }
        
        // squares
        cout << "squares\n";
        for(int sr=0; sr<3; sr++)
            for(int sc=0; sc<3; sc++)
            {
                for(int i=0; i<3; i++)
                    for(int j=0; j<3; j++)
                        ms.insert(board[sr*3+i][sc*3+j]);
                if(! validateSet())
                    return false;
                ms.clear();
            }
        return true;
    }
};
