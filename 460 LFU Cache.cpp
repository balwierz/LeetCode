class LFUCache {
    unordered_map<int, pair<int, int>> key2count;    // key --> (count, lastUsed)
    map<pair<int, int>, pair<int, int>> count2val;   // (count, lastUsed) --> (key, value)
    int bufSize;
    int numElem;
    int time;
public:
    LFUCache(int capacity) : bufSize(capacity)
    {
        numElem = 0;
        time = 0;
    }
    
    int get(int key)
    {
        auto count_used = key2count.find(key);
        if(count_used == key2count.end())
        {
            return -1;
        }
        auto key_val = count2val[count_used->second];
        int ret = key_val.second;
        int count = count_used->second.first;
        count2val.erase(count_used->second);

        count2val[make_pair(count+1, time)] = key_val;
        key2count[key] = make_pair(count+1, time);
        time++;
        return ret;
    }
    
    void put(int key, int value)
    {
        if(bufSize == 0) return;
        auto it = key2count.find(key);
        if(numElem >= bufSize && it == key2count.end())
        {
            // need to remove the LFU element:
            auto it2 = count2val.begin();
            key2count.erase(it2->second.first);   // old LFU key to remove
            count2val.erase(it2);
        }
        // add the new element
        if(it == key2count.end())   // need to create a new element
        {
            auto p = make_pair(1, time);
            count2val[p] = make_pair(key, value);
            key2count[key] = p;
            numElem++;
        }
        else   // update an existing element
        {
            auto curCount = key2count[key];
            // delete the old one:
            count2val.erase(curCount);
            curCount.first ++;
            curCount.second = time;
            count2val[curCount] = make_pair(key, value);
            key2count[key] = curCount;
        }
        // 
        time++;
    }
};
