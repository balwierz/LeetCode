class Solution {
public:
    int score(vector<int> &p)
    {
        int ret = 0;
        int ten = 0;
        for(int &a : p)
        {
            ret += a;
            if(ten > 0)
                ret += a;
            ten --;
            if(a == 10)
                ten = 2;
        }
        return ret;
    }
    int isWinner(vector<int>& player1, vector<int>& player2) 
    {
        int s1 = score(player1);
        int s2 = score(player2);
        if(s1 == s2)
            return 0;
        return s1 > s2 ? 1 : 2;
    }
};
