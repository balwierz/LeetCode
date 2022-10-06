class TimeMap {
    unordered_map<string, map<int, string>> key2map;
public:
    TimeMap() { }
    
    void set(string key, string value, int timestamp)
    {
        key2map[key][timestamp] = value;
    }
    
    string get(string key, int timestamp)
    {
        auto lb = key2map[key].upper_bound(timestamp);
        if(lb == mp.begin())
            return "";
        lb--;
        return lb->second;
    }
};
