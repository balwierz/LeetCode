class RandomizedSet 
{
    unordered_map<int, int> val2ind;
    vector<int> ind2val;
public:
    RandomizedSet() 
    {
        //srand(time(NULL));
    }
    
    bool insert(int val)
    {
        if(val2ind.find(val) == val2ind.end())
        {
            ind2val.push_back(val);
            val2ind[val] = ind2val.size()-1;
            return true;
        }
        else
        {
            return false;
        }
    }
    
    bool remove(int val)
    {
        auto it = val2ind.find(val);
        if(it == val2ind.end())
        {
            return false;
        }
        else
        {
            int ind = it->second;
            int last = *(ind2val.rbegin());
            ind2val[ind] = last;
            val2ind[last] = ind;
            val2ind.erase(it);
            ind2val.pop_back();
            return true;
        }
    }
    
    int getRandom() 
    {
        cout << ind2val.size() << endl;
        int ind = rand() % ind2val.size();
        return ind2val[ind];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
