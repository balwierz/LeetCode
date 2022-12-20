class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) 
    {
        int n = rooms.size();
        unordered_set<int> keys = {0};
        vector<bool> visited(n, false);
        while(keys.size())
        {
            unordered_set<int> newKeys;
            for(int key : keys)
            {
                //cout << "key " << key << endl;
                visited[key] = true;
                for(int key2 : rooms[key])
                {
                    if(! visited[key2] && ! keys.count(key2))
                        newKeys.insert(key2);
                }
            }
            keys = newKeys;
        }
        return all_of(visited.begin(), visited.end(), [](bool l){return l;});
    }
};
