class Solution {
    vector<vector<pair<int, char>>> children;
    unordered_map<int, int> bitmap2count;
public:
    void dfs(int node, int bitmap)
    {
        bitmap2count[bitmap] ++;
        for(pair<int, char> &child : children[node])
        {
            int b = (1 << (child.second - 'a')) ^ bitmap;
            dfs(child.first, b);
        }
    }
    long long countPalindromePaths(vector<int>& parent, string s)
    {
        int n = parent.size();
        children = vector<vector<pair<int, char>>>(n, vector<pair<int, char>>());
        for(int i=1; i<n; i++)
        {
            children[parent[i]].emplace_back(i, s[i]);
        }
        dfs(0, 0);
        long long nPairs = 0; // includes self pairs and pairs in both orders, ab, ba
        for(auto [bitmap, count] : bitmap2count)
        {
            // identical:
            nPairs += (long long)count*count;
            // diffrent by one:
            for(int i = 0; i<26; i++)
            {
                auto it = bitmap2count.find(bitmap ^ (1<<i));
                if(it != bitmap2count.end())
                    nPairs += (long long)count * it->second;
            }
        }
        return (nPairs-n) / 2;
    }
};
