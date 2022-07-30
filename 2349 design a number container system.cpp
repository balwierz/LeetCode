class NumberContainers
{
    unordered_map<int, int> ind2num;
    unordered_map<int, set<int>> num2indSet;
public:
    /*NumberContainers()
    {
    }*/
    
    void change(int index, int number)
    {
        auto it = ind2num.find(index);
        if(it != ind2num.end() )
        {
            // the index is already used
            // remove it from the set:
            int oldNum = it->second;
            num2indSet[oldNum].erase(index);
            ind2num.erase(index);
        }
        // add it to the new set:
        num2indSet[number].insert(index);
        // update ind to num
        ind2num[index] = number;
    }
    
    int find(int number)
    {
        auto it = num2indSet.find(number);
        if(it != num2indSet.end())
        {
            auto it2 = it->second.begin();
            if(it2 != it->second.end())
                return *it2;
        }
        return -1;
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
