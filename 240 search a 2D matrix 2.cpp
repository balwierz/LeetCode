class Solution {
    bool search(vector<vector<int>> &m, int r0, int r1, int c0, int c1, int target)
    {
        //cout << r0 << "-" << r1 << "  " << c0 << "-" << c1 << endl;
        // we use jim kent indexing
        if(r0>=r1 || c0>=c1)
            return false;
        if(r1-r0 == 1 && c1-c0 == 1)
            return m[r0][c0] == target;
        
        int rPivot = (r1-r0)/2 + r0;   // rPivot to rPivot+1
        int cPivot = (c1-c0)/2 + c0;
        int pivot  = m[rPivot][cPivot];
        
        if(pivot == target)
            return true;
        if(target < pivot)
        {
            return
            search(m, r0, rPivot, c0, cPivot, target) ||
            search(m, rPivot, r1, c0, cPivot, target) ||
            search(m, r0, rPivot, cPivot, c1, target);
        }
        else  // pivot < target
        {
            return
            search(m, rPivot+1, r1, cPivot+1, c1, target) ||
            search(m, r0, rPivot+1, cPivot+1, c1, target) ||
            search(m, rPivot+1, r1, c0, cPivot+1, target);
        }
    }
    
    bool search2(vector<vector<int>> &m, int target)
    {
        ios::sync_with_stdio(0);
        int i = 0;
        int j = m[0].size()-1;
        int elem;
        while(i<m.size() && j>=0 && (elem = m[i][j]) != target)
        {
            if(elem > target)
                j--;
            else
                i++;
        }
        if(i<m.size() && j>=0)
            return true;
        return false;
    }
    
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        // this is slow for this size of data.
        // but it is O(log n + log m)
        //return search(matrix, 0, matrix.size(), 0, matrix[0].size(), target);
        
        // this is O(n+m), but faster
        return search2(matrix, target);
    }
};
