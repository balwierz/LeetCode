class Solution {
public:
    int minimumCost(vector<int>& start, vector<int>& target, vector<vector<int>>& specialRoads) 
    {
        if(start == target) return 0;
        multimap<int, pair<int,int>> dist2pos;
        map<pair<int,int>, vector<vector<int>>> pos2roads; // [vals: x, y, len]
        set<pair<int,int>> unvisited;
        for(vector<int> &v : specialRoads)
        {
            pos2roads[make_pair(v[0], v[1])].push_back({v[2], v[3], v[4]});
            dist2pos.insert({abs(v[0]-start[0]) + abs(v[1]-start[1]), {v[0], v[1]}}); // to road beginnings
            dist2pos.insert({abs(v[2]-start[0]) + abs(v[3]-start[1]), {v[2], v[3]}}); // to road ends
            unvisited.insert({v[0], v[1]});
            unvisited.insert({v[2], v[3]});
        }
        dist2pos.insert({abs(target[0]-start[0]) + abs(target[1]-start[1]), {target[0], target[1]}}); // to target
        unvisited.insert({target[0], target[1]});
        while(true)
        {
            // get the closest element:
            auto it = dist2pos.begin();
            //cout << "trying " << it->second.first << ", " << it->second.second << " with distance " << it->first << endl;
            if(unvisited.find(it->second) == unvisited.end()) // pos visited
            {
                //cout << "   but it was visited" << endl;
                dist2pos.erase(it);
                continue;
            }
            int curDist = it->first;
            pair<int, int> &curPos = it->second;
            unvisited.erase(curPos); // mark visited
            if(curPos.first == target[0] && curPos.second == target[1])
                return curDist;
            // process all unvisited elements:
            for(auto &u : unvisited)
            {
                dist2pos.insert({curDist+abs(curPos.first - u.first)+abs(curPos.second - u.second), u});
            }
            // process all roads from here:
            for(auto &road : pos2roads[curPos])
            {
                auto destinationIt = unvisited.find({road[0], road[1]});
                if(destinationIt != unvisited.end())  // destination is unvisited
                    dist2pos.insert({curDist+road[2], {road[0], road[1]}});
            }
            dist2pos.erase(it);
        }
        return 0;
    }
};
