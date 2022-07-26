class Solution {
    int GCD(vector<int> &num)
    {
        if(num.size() == 1)
            return num[0];
        int a = num.back();
        num.pop_back();
        while(num.size())
        {
            int b = num.back();
            num.pop_back();
            while(a != 0 and b != 0)
            {
                if(a > b)
                    a %= b;
                else
                    b %= a;
            }
            if(a == 0)
                a = b;
        }
        return a;
    }
public:
    int minOperations(vector<int>& nums, vector<int>& numsDivide)
    {
        // 1:
        int d = GCD(numsDivide);  // my own function
        
        // 2:
        //int d = numsDivide[0];
        //for(int k : numsDivide)
        //    d = gcd(d, k);
        
        // 3:
        //int d = accumulate(numsDivide.begin(), numsDivide.end(), numsDivide[0],
        //                   [](int &a, int &b) { return gcd(a,b); });
        
        // first pass: find the smallest element dividing d
        int s = 1000000001;
        for(int num : nums)
        {
            if(d % num == 0)
                if(num < s)
                    s = num;
        }
        if(s == 1000000001)
            return -1;
        //cout << s;
        // second pass: find the number of elements smaller than s
        int ret = 0;
        for(int num : nums)
        {
            if(num < s)
                ret++;
        }
        return ret;
    }
};
