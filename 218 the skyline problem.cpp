class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& b)
    {
        priority_queue<pair<int, int>> q;
        int h = 0;
        int thisEnd = INT_MAX;
        int i = 0;
        int n = b.size();
        vector<vector<int>> ret;
        while(i < n || q.size())
        {
            //cout << i << endl;
            while(i<n && b[i][0] <= thisEnd)
            {
                int thisStart = b[i][0];
                while(i<n && b[i][0] == thisStart)
                {
                    q.emplace(b[i][2], b[i][1]);
                    i++;
                }
                int newH = q.top().first;
                if(newH > h)  // we have a new tallest building
                {
                    thisEnd = q.top().second;
                    h = newH;
                    ret.push_back({thisStart, h});
                    //cout << "a[" << thisStart << ", " << h << "]" << endl;
                }
                else if(newH == h)
                {
                    thisEnd = max(thisEnd, q.top().second);
                }
                
            }
            //cout << "i" << q.size() << endl;
            // now we have an end coming
            //q.pop(); // we ignore the values as they are h and thisEnd
            auto t = q.top();  int nextH = t.first; int nextE = t.second;
            
            while(q.size() && nextE <= thisEnd)
            {
                //cout << "e" << q.size() << endl;
                q.pop();
                if(q.size())
                {
                    auto t = q.top(); 
                    nextH = t.first; 
                    nextE = t.second;
                }
            }
            if(! q.size())
            {
                nextH = 0;
                nextE = INT_MAX;
            }
            ret.push_back({thisEnd, nextH});
            //cout << "q[" << thisEnd << ", " << nextH << "]" << endl;
            thisEnd = nextE;
            h = nextH;
        }
        return ret;
    }
};
