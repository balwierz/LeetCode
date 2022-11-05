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
    TrieNode root;
public:
    Trie()
    {
    }
    
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
    
    bool search(string word)
    {
        auto it = &root;
        for(char c : word)
        {
            c -= 'a';
            if(it->child[c])
                it = it->child[c];
            else
                return false;
        }
        return it->isEnd;
    }
    
    bool startsWith(string prefix) 
    {
        auto it = &root;
        for(char c : prefix)
        {
            c -= 'a';
            if(it->child[c])
                it = it->child[c];
            else
                return false;
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
