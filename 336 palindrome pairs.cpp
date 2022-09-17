class Solution
{
public:
    vector<vector<int>> palindromePairs(vector<string>& words) 
    {
        map<int,unordered_map<string,int>> memo;
        for(int g=0;g<words.size();g++)
        {
            string str = string( words[g].rbegin() , words[g].rend() );
            memo[ words[g].size() ][ str ] = g;
        }
        
        auto check = [&](string& str,int i,int j) -> bool
        {
            while( i < j )
            {
                if( str[i] != str[j] ) break;
                i++;
                j--;
            }
            return i >= j;
        };
        
        vector<vector<int>> res;
        for(int g=0;g<words.size();g++)
        {    
            string& str = words[g];   
            for(auto& p : memo)
            {
                if( p.first > str.size() ) 
                    break;
                if( p.first == str.size() )
                {    
                    if( p.second.count(str) && p.second[str] != g )
                        res.push_back( { g , p.second[str] } );
                    continue;
                }
                
                if( check( str , 0 , words[g].size()-1 - p.first ) && 
                   p.second.count( words[g].substr(words[g].size()-p.first) ) )
                {
                    // cout<<"first"<<endl;
                    res.push_back( { p.second[ words[g].substr( words[g].size()-p.first ) ] , g } );
                }
                
                if( check( str , words[g].size() - ( words[g].size() - p.first ) , words[g].size()-1 ) &&
                   p.second.count( words[g].substr( 0 , p.first ) ) )
                {
                    // cout<<"second"<<endl;
                    res.push_back( { g , p.second[ words[g].substr( 0 , p.first ) ] } );
                }
            }
        }
        return res;
    }
};

class Solution4 {
private:
    bool isP(string &s, int left, int right)
    { // check if s[left::right] is a palindrome
        while(left<right)
            if(s[left++] !=s[right--]) return false;
        return true;
    }

public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        unordered_map<string, int> map;
        set<int> wLen;
        int it, len=words.size(), it2, sL, lL;
        vector<vector<int>> res;

        for(it=0; it<len; ++it) { //build map and the length set
            map[words[it]] = it;
            wLen.insert(words[it].size());
        }

        for(it=0; it<len; ++it)
        { // for each string
            string temp = words[it];
            lL = temp.size();
            std::reverse(temp.begin(), temp.end()); // reverse it, step a)
            if(map.count(temp) && map[temp]!=it)
                  res.push_back(vector<int>({it, map[temp]})); //step b)
            auto itC = wLen.find(words[it].size());
            for(auto itL=wLen.begin(); itL!=itC; ++itL)
            { // for each possible shorter length
                sL = *itL;
                if(isP(temp, 0, lL-sL-1) && map.count(temp.substr(lL-sL)))
                      res.push_back(vector<int>({it, map[temp.substr(lL-sL)]})); //step c1)
                if(isP(temp, sL, lL-1) && map.count(temp.substr(0,sL)))
                     res.push_back(vector<int>({map[temp.substr(0,sL)], it})); //step c2)                       
            }
        }    
        return res;
    }
};



struct TrieNode {
    TrieNode *next[26] = {};
    int index = -1;
    vector<int> palindromeIndexes;
};

class Solution3 {
    TrieNode root; // Suffix trie
    void add(string &s, int i) {
        auto node = &root;
        for (int j = s.size() - 1; j >= 0; --j) {
            if (isPalindrome(s, 0, j)) node->palindromeIndexes.push_back(i); // A[i]'s prefix forms a palindrome
            int c = s[j] - 'a';
            if (!node->next[c]) node->next[c] = new TrieNode();
            node = node->next[c];
        }
        node->index = i;
        node->palindromeIndexes.push_back(i); // A[i]'s prefix is empty string here, which is a palindrome.
    }
    
    bool isPalindrome(string &s, int i, int j) {
        while (i < j && s[i] == s[j]) ++i, --j;
        return i >= j;
    }
    
public:
    vector<vector<int>> palindromePairs(vector<string>& A) {
        int N = A.size();
        for (int i = 0; i < N; ++i) add(A[i], i);
        vector<vector<int>> ans;
        for (int i = 0; i < N; ++i) {
            auto s = A[i];
            auto node = &root;
            for (int j = 0; j < s.size() && node; ++j) {
                if (node->index != -1 && node->index != i && isPalindrome(s, j, s.size() - 1)) ans.push_back({ i, node->index }); 
                // A[i]'s prefix matches this word and A[i]'s suffix forms a palindrome
                node = node->next[s[j] - 'a'];
            }
            if (!node) continue;
            for (int j : node->palindromeIndexes) { 
                // A[i] is exhausted in the matching above. 
                // If a word whose prefix is palindrome after matching its suffix with A[i], 
                // then this is also a valid pair
                if (i != j) ans.push_back({ i, j });
            }
        }
        return ans;
    }
};




class Solution2 {
    bool checkPalindrome(const string &str, int left, int right)
    {
        // checks if there is a palindrome str[left...right] (non inclusive)
        right --;
        while(left<right)
        {
            if(str[left++] != str[right--])
                return false;
        }
        return true;
    }
public:
    vector<vector<int>> palindromePairs(vector<string>& words)
    {
        set<vector<int>> ret;
        unordered_map<string, int> wordsRev;
        for(int i=0; i<words.size(); i++)
        {
            string w = words[i];
            reverse(w.begin(), w.end());
            wordsRev[w] = i;
        }
        for(int wI = 0; wI < words.size(); wI++)
        {
            int i=0, j=0;  // iterators of the central (possibly palindromic part)
            auto &w = words[wI];
            for( ; j<=w.size(); j++)
            {
                auto it=wordsRev.find(w.substr(j, w.size()-j));
                if(it != wordsRev.end() && checkPalindrome(w, 0, j))
                {
                        if(it->second != wI)
                            ret.insert({it->second, wI});
                }
            }
            for( ;i<=w.size(); i++)
            {
                auto it=wordsRev.find(w.substr(0, i));
                if(it != wordsRev.end() && checkPalindrome(w, i, w.size()))
                {
                        if(it->second != wI)
                            ret.insert({wI, it->second});
                }
            }
        }
        vector<vector<int>> ret2;
        for(auto &k : ret)
            ret2.push_back(k);
        return ret2;
    }
};
