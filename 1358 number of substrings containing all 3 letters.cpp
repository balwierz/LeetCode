class Solution {
    public:
    int numberOfSubstrings(string s)
    {
        int a=0, b=0, c=0;
        int i=0, j=0;
        int n=s.size();
        //cout << "n=" << n << endl;
        int ret = 0;
        while(j<n && i<n)
        {
            while(!a || !b || !c)
            {
                
                if(s[i]=='a')
                    a++;
                if(s[i]=='b')
                    b++;
                if(s[i]=='c')
                    c++;
                i++;
                if(i==n)
                    break;
            }
            //cout << "i=" << i << endl;
            //cout << "a" << a << " b" << b << " c" << c << endl;
            while(a && b && c)
            {
                ret += n-i+1;
                //cout << "adding " << n-i+1 << endl;
                if(s[j]=='a')
                    a--;
                if(s[j]=='b')
                    b--;
                if(s[j]=='c')
                    c--;
                j++;
                if(j==n)
                    break;
            }
        }
        return ret;
    }
};
