class Solution {
public:
    int editDist(const string &a, const string &b)
    {
        int ret = 0;
        for(int i=0; i<a.size(); i++)
        {
            if(a[i] != b[i])
                if(++ret > 1) return ret;
        }
        return ret;
    }
    vector<vector<string>> recreate(int node, vector<vector<int>> &backSteps, vector<string> &wordList)
    {
        vector<vector<string>> ret;
        //cout << "recreate " << wordList[node] << endl;
        if(node == 0)
            return vector<vector<string>>(1, vector<string>(1, wordList[0]));
        for(int prev : backSteps[node])
        {
            vector<vector<string>> pu = recreate(prev, backSteps, wordList);
            ret.insert(ret.end(), pu.begin(), pu.end());
        }
        for(int i=0; i<ret.size(); i++)
        {
            ret[i].push_back(wordList[node]);
        }
        return ret;
    }
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) 
    {
        // make a graph
        wordList.insert(wordList.begin(), beginWord);  // O(n)
        vector<vector<int>> neigh(wordList.size());
        int whichEnd = -1;
        for(int i=0; i<wordList.size(); ++i)
        {
            for(int j=i+1; j<wordList.size(); j++)
                if(editDist(wordList[i], wordList[j]) == 1)
                {
                    neigh[i].push_back(j);
                    neigh[j].push_back(i);
                }
            if(wordList[i] == endWord)
                whichEnd = i;
        }
        if(whichEnd == -1)
            return vector<vector<string>>(0);
        // bfs search the graph
        bool foundEnd = false;
        //vector<vector<vector<string>>> paths(wordList.size());
        vector<vector<int>> backSteps(wordList.size());
        // [endpoint][soulutio#][stringI]
        unordered_set<int> nextLayer[2];
        // key is: node id, value is: list 
        int layerParity = 0;
        nextLayer[0].insert(0);
        //paths[0].push_back(vector<string>{beginWord});
        vector<bool> visited(wordList.size(), false);
        while(! foundEnd && ! nextLayer[layerParity].empty())
        {
            //cout << "layer" << endl;
            while(! nextLayer[layerParity].empty())
            {
                auto it = nextLayer[layerParity].begin();
                int node = *it;
                nextLayer[layerParity].erase(it);
                
                visited[node] = true;
                //cout << "Node " << node << " " << wordList[node] << endl;
                // add all non-visited neighbours to the next layer and increase their paths
                for(int nn : neigh[node])
                {
                    if(! visited[nn] && ! nextLayer[layerParity].count(nn))
                    {
                        /*
                        for(auto p : paths[node])
                        {
                            p.push_back(wordList[nn]);
                            paths[nn].push_back(p);
                        }
                        */
                        if(node == whichEnd)
                            foundEnd = true;
                        nextLayer[1 - layerParity].insert(nn);
                        backSteps[nn].push_back(node);
                    }
                }
            }
            layerParity = 1 - layerParity;   // swap sets
        }
        // recreate all paths:
        return recreate(whichEnd, backSteps, wordList);
        //return paths[whichEnd];
    }
};
