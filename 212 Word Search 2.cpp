class TrieNode
{
public:
    bool isEnd;
    TrieNode* child[26];
    TrieNode()
    {
        isEnd = false;
        for(int i=0; i<26; i++)
            child[i] = nullptr;
    }
};

class Trie 
{
public:
    TrieNode root;

    void insert(string word)
    {
        auto it = &root;
        for(char c : word)
        {
            c -= 'a';
            if(! it->child[c])
            {
                it->child[c] = new TrieNode;
            }
            it = it->child[c];
        }
        it->isEnd = true;
    }
};

class Solution 
{
    int m, n;
    vector<pair<int,int>> dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    vector<vector<char>> board;
    Trie trie;
    unordered_set<string> seen;
    vector<vector<bool>> visited;
    string cand;
    
    void helper(int x, int y, TrieNode *it)
    {
        cand += board[x][y];       
        visited[x][y] = true;
        
        if(it->isEnd)
            seen.insert(cand);
        
        for(pair<int,int> dir : dirs)
        {
            int xx = x + dir.first;
            int yy = y + dir.second;
            if(xx < 0 || xx >= m || yy < 0 || yy >= n)
                continue;
            // this step is in the board
            if(it->child[board[xx][yy]-'a'] && ! visited[xx][yy])
            {
                helper(xx, yy, it->child[board[xx][yy]-'a']);
            }
        }
        // backtrack
        visited[x][y] = false;
        cand.pop_back();
    }
    
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words)
    {
        // init
        m = board.size(), n = board[0].size();
        this->board = board;
        visited = vector<vector<bool>>(m, vector<bool>(n, false));

        // insert all words to trie
        for(auto w : words)
            trie.insert(w);
        
        // try every position (i,j) as starting
        for(int i=0; i<m; i++) for(int j=0; j<n; j++)
        {
            if(trie.root.child[board[i][j]-'a'])
            {
                helper(i, j, trie.root.child[board[i][j]-'a']);
            }
        }
        
        // transform set to a vector
        vector<string> ret;
        for(auto s : seen)
            ret.push_back(s);
        return ret;
    }
};

