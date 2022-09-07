class Solution {
    vector<vector<int>> *grid;
    int n;
public:
    int mark(int i, int j, int id)
    {
        //cout << i << ',' << j << endl;
        int ret = 0;
        if(i<0 || j<0 || i>=n || j >=n)
            return 0;
        if((*grid)[i][j] == 0)
            return 0;
        if((*grid)[i][j] == 1)
        {
            ret++;
            (*grid)[i][j] = id;
            ret += mark(i-1, j, id);
            ret += mark(i+1, j, id);
            ret += mark(i, j-1, id);
            ret += mark(i, j+1, id);
        }
        return ret;
    }
    int largestIsland(vector<vector<int>>& grid)
    {
        this->grid = &grid;
        vector<int> isl2size;
        isl2size.push_back(0); //0
        isl2size.push_back(0); //1
        int islC = 2;
        n = grid.size();
        for(int i=0; i<n; i++)
            for(int j=0; j< n; j++)
                if(grid[i][j] == 1)
                    isl2size.push_back(mark(i, j, islC++));
        //for(auto i: isl2size)
        //    cout << i << " ";
        if(islC == 2)  // no islands
            return 1;
        if(isl2size[2] == n*n)
            return n*n;  //one big island
        int ret = 0;
        for(int i=0; i<n; i++)
            for(int j=0; j< n; j++)
                if(grid[i][j] == 0)
                {
                    unordered_set<int> s;
                    if(i>0)
                        s.insert(grid[i-1][j]);
                    if(j>0)
                        s.insert(grid[i][j-1]);
                    if(i<n-1)
                        s.insert(grid[i+1][j]);
                    if(j<n-1)
                        s.insert(grid[i][j+1]);
                    int w = 1;
                    for(int isl:s)
                        w += isl2size[isl];
                    ret = max(ret, w);
                }
        
        return ret;
    }
};
