class Solution {
    int n;
    vector<char> colour;
    vector<vector<int>> *g;
public:
    bool dfs(int u, char col=1)
    {
        colour[u] = col;
        //cout << u << " is " << (int)col << endl;
        char otherCol = col==1 ? 2 : 1;
        for(auto v: (*g)[u])
        {
            if(colour[v] == 0)
            {
                //cout << u << "->" << v << " " << (int)col << "," << (int)otherCol << endl;
                if(dfs(v, otherCol) == false)
                    return false;
            }
            else if(colour[v] == col)
                return false;
        }
        //cout << "finished " << u << endl;
        return true;
    }
    bool isBipartite(vector<vector<int>>& graph)
    {
        n = graph.size();
        colour = vector<char>(n, 0);
        g = &graph;
        for(int i=0; i<n; i++)
        {
            if(colour[i] == 0)
            {
                //cout << "start " << i << endl;
                if(!dfs(i))
                    return false;
            }
        }
        return true;
    }
}; 
