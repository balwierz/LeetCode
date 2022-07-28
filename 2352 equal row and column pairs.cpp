class Solution {
    class Vec
    {
        vector<int> v;
        public:
        char rowcol;
        bool operator<(const Vec &other) const
        {
            return v < other.v;
        }
        /*bool operator<(const Vec &other) const
        {
            auto it1 = v.begin(), it2 = other.v.begin();
            for(; it1<v.end(); it1++, it2++)
            {
                if(*it1 != *it2)
                    break;
            }
            if(it1 == v.end())
                return false;
            return *it1 < *it2;
        }*/
        public:
        Vec(const vector<int> &w, char c) : v(w), rowcol(c) {}
    };
public:
    int equalPairs(vector<vector<int>>& grid)
    {
        multiset<Vec> ms;
        for(const vector<int> &w : grid) //(grid.begin(), grid.end());
            ms.insert(Vec(w, 'r'));
        for(int i=0; i<grid.size(); i++)
        {
            vector<int> tmp;
            for(int j=0; j<grid.size(); j++)
            {
                tmp.push_back(grid[j][i]);
            }
            ms.insert(Vec(tmp, 'c'));
        }
        int ret = 0;
        for(auto it=ms.begin(); it!=ms.end(); )
        {
            auto [first, last] = ms.equal_range(*it);
            int colN = 0, rowN = 0;
            for(auto it2=first; it2!=last; it2++)
            {
                if(it2->rowcol == 'c')
                    colN++;
                else
                    rowN++;
            }
            ret += colN * rowN;
            it = last;
        }
        return ret;
    }
};
