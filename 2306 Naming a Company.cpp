class Solution {
public:
    long long distinctNames(vector<string>& ideas)
    {
        // transform ideas into a bool matrix [ending][first_letter]
        unordered_map<string, vector<bool>> data;
        vector<bool> firstLetter(26, false);
        for(string& word : ideas)
        {
            char lett = word[0];
            string ending = word.substr(1);
            if(data.find(ending) == data.end()) // init if necesary
                data[ending] = vector<bool>(26, false);
            data[ending][lett-'a'] = true;
            firstLetter[lett-'a'] = true;
        }
        vector<char> allLetters;
        for(int i=0; i<26; i++)
            if(firstLetter[i])
                allLetters.push_back(i);
        
        // keep counting letter pairs such that the first is present and the second is not
        vector<vector<int>> dp(26, vector<int>(26, 0));
        long long ret = 0;
        for(auto &w : data)  // for each ending
        {
            int i = 0, j = 0;
            char bufPos[26], bufNeg[26];
            for(char c : allLetters)
                if(w.second[c])  // present with this ending
                    bufPos[i++] = c;
                else
                    bufNeg[j++] = c;
            for(int k=0; k<i; k++)
                for(int l=0; l<j; l++)
                {
                    ret += dp[bufNeg[l]][bufPos[k]];
                    dp[bufPos[k]][bufNeg[l]] ++;
                }
        }
        return ret*2;
    }
};
