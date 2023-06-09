class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) 
    {
        int i = -1;
        int j = letters.size();
        while(i+1<j)
        {
            int mid = (i+j)/2;
            if(letters[mid] <= target)
                i = mid;
            else
                j = mid;
        }
        if(j == letters.size())
            return letters[0];
        else
            return letters[j];
    }
};
