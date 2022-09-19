vector<string> split (const string &s, char delim) 
{
    vector<string> result;
    stringstream ss (s);
    string item;
    while (getline (ss, item, delim))
    {
        result.push_back (item);
    }
    return result;
}


class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths)
    {
        unordered_map<string, vector<string>> bigMap;
        for(auto &ls : paths)
        {
            vector<string> v = split(ls, ' ');
            string path = v[0];
            for(int i=1; i<v.size(); i++)
            {
                v[i].pop_back();
                vector<string> fileName_cont = split(v[i], '(');
                bigMap[fileName_cont[1]].push_back(path + "/" + fileName_cont[0]);
            }
        }
        vector<vector<string>> ret;
        for(auto it=bigMap.begin(); it !=bigMap.end(); it++)
        {
            auto &fileList = it->second;
            if(fileList.size() > 1)
                ret.push_back(fileList);
        }
        return ret;
    }
};
