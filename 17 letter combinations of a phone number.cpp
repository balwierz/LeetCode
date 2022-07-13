class Solution
{
    vector<string> letters{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
public:
    vector<string> letterCombinations(string digits)
    {
        vector<string> strings{""};
        if(! digits.size())
            return vector<string>(0);
        for(int i=0; i<digits.size(); i++)
        {
            string chars = letters[digits[i]-'2'];
            vector<string> r;
            for(int j=0; j<chars.size(); j++)
            {
                for(auto it=strings.begin(); it<strings.end(); it++)
                {
                    r.push_back(*it+chars[j]);
                }
            }
            strings = r;
        }
        return strings;
    }
};
