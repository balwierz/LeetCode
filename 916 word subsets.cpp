class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2)
    {
        char bigUnion[128] = {0};
        char tmpUnion[128] = {0};
        vector<string> ret;
        for(string w:words2)
        {
            //memset(tmpUnion+'a', 0, 26);
            for(char i='a'; i<='z'; i++)
                tmpUnion[i] = 0;
            for(char letter:w)
                tmpUnion[letter] ++;
            for(char i='a'; i<='z'; i++)
                if(tmpUnion[i] > bigUnion[i])
                    bigUnion[i] = tmpUnion[i];
        }
        for(string w:words1)
        {
            //memset(tmpUnion+'a', 0, 26);
            for(char i='a'; i<='z'; i++)
                tmpUnion[i] = 0;
            for(char letter:w)
                tmpUnion[letter] ++;
            bool fGood = true;
            for(char i='a'; i<='z'; i++)
                if(tmpUnion[i] < bigUnion[i])
                {
                    fGood = false;
                    break;
                }
            if(fGood)
                ret.push_back(w);
        }
        return ret;
    }
};
