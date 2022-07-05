class Solution {
    static bool isVowel(char c)
    {
        return(c=='a' || c=='e' || c=='i' || c=='o' || c=='u');
    }
public:
    long long countVowels(string word) 
    {
        long long ret = 0;
        long long colSum = 0;
        for(int i=0; i<word.size(); i++)
        {
            if(isVowel(word[i]))
                colSum += (i+1);
            ret += colSum;
        }
        return ret;
    }
};
