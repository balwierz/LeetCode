class Solution {
public:
    string addBinary(string a, string b)
    {
        int carry = 0;
        auto aI = a.rbegin();
        auto bI = b.rbegin();
        string ret;
        while(aI != a.rend() || bI != b.rend() || carry)
        {
            int an = aI != a.rend() ? *aI - '0' : 0;
            int bn = bI != b.rend() ? *bI - '0' : 0;
            int d = (an + bn + carry) % 2;
            carry = (an + bn + carry) / 2;
            ret += d ? '1' : '0';
            if(aI != a.rend())
                aI++;
            if(bI != b.rend())
                bI++;
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
