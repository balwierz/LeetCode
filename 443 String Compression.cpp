int compress(vector<char>& chars) 
{
    int i = 0, j = 0;
    while(true)
    {
        if(j == chars.size())
            return i;
        char letter = chars[j++];
        int num = 1;
        while(j < chars.size() && chars[j] == letter)
            { num++; j++; }
        chars[i++] = letter;
        if(num > 1)
            for(char c : to_string(num))
                chars[i++] = c;
    }
}
