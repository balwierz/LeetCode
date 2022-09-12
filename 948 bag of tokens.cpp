class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power)
    {
        sort(tokens.begin(), tokens.end());
        int score = 0, n = tokens.size();
        int i=0, j=n-1;
        while(i<j)
        {
            while(power >= tokens[i])
            {
                score ++;
                power -= tokens[i++];            }
            if(i<j && score>0) // there are at least 2 more unused tokens in the middle
            {
                score --;
                power += tokens[j--];
            }
            else
                break;
        }
        if(n>0 && power >= tokens[i])
            score ++;
        return score;
    }
};
