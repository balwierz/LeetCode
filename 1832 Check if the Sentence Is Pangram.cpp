class Solution {
public:
    bool checkIfPangram(string sentence)
    {
        vector<int> cnt(256, 0);
        for(char c : sentence)
            cnt[c]++;
        for(int i='a'; i<='z'; i++)
            if(cnt[i] == 0)
                return false;
        return true;
    }
};
