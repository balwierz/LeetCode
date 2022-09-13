class Solution {
public:
    bool validUtf8(vector<int>& d)
    {
        vector<char> data(d.begin(), d.end());
        int n = data.size();
        for(int i=0; i<n; i++)
        {
            if((0x80 & data[i]) == 0)  // single byte
                continue;
            int b = 0;
            if((0xE0 & data[i]) == 0xC0) // two bytes
                b = 1;
            else if((0xF0 & data[i]) == 0XE0)  // three
                b = 2;
            else if((0xF8 & data[i]) == 0xF0) // four
                b = 3;
            if(b==0)
                return false;
            while(b--)
            {
                if(++i == n)
                    return false;
                if((0xC0 & data[i]) != 0x80)
                    return false;
            } 
        }
        return true;
    }
};
