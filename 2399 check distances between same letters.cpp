class Solution {
public:
    bool checkDistances(string s, vector<int>& distance)
    {
        
        vector<int> firstPos(26, -1);
        for(int i=0; i<s.size(); i++)
        {
            if(firstPos[s[i]-'a'] == -1)
                firstPos[s[i]-'a'] = i;
            else if( i - firstPos[s[i]-'a'] -1 != distance[s[i]-'a'])
                return false;
        }
        return true;
    }
};
