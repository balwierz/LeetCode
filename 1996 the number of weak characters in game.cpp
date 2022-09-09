class Solution {
public:
    int numberOfWeakCharacters(vector<vector<int>>& p) 
    {
        int n = p.size();
        sort(p.begin(), p.end(), [](vector<int> &a, vector<int> &b) { return a[0] > b[0]; });
        int outlineC = 0;
        int lastX = 0;
        for(int i=0; i<n; )
        {
            int thisY = p[i][0];
            int thisX = lastX;
            while(i<n && p[i][0] == thisY)
            {
                //cout << p[i][0] << " " << p[i][1]  << "\t" << thisY << " " << thisX << endl;
                if(p[i][1] >= lastX)
                    outlineC++;
                thisX = max(p[i][1], thisX);
                i++;
            }
            lastX = thisX;
        }
        return n-outlineC;
    }
};
