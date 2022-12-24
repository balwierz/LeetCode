class Solution {
public:
    vector<int> cycleLengthQueries(int n, vector<vector<int>>& queries) 
    {
        vector<int> ret(queries.size());
        for(int i=0; i<queries.size(); i++)
        {
            // calculate the  number
            // of leading zeroes
            int a = queries[i][0];
            int b = queries[i][1];
            int az = __builtin_clz(a);
            int bz = __builtin_clz(b);
            while(az < 32 && bz < 32 && ((a >> (31-az)) & 1) == ((b >> (31-bz)) & 1))
            {
                az++; bz++;
            }
            ret[i] = (32 - az + 32 - bz + 1);
        }
        return ret;
    }
};
