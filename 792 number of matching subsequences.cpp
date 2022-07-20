class Solution {
    struct elem
    {
        int wordIndex;
        int charIndex;
        elem(const int& w, const int& c) : wordIndex(w), charIndex(c) {}
    };
public:
    int numMatchingSubseq(string s, vector<string>& words)
    {
        forward_list<elem> tab[26];
        // init
        for(int w = 0; w<words.size(); w++)
        {
            int letter = words[w][0] - 'a';
            elem e(w, 0);
            tab[letter].push_front(e);
        }
        int ret = 0;
        
        // main loop
        for(int sI=0; sI<s.size(); sI++)
        {
            int letter = s[sI] - 'a';
            forward_list<elem> newList;
            while(!tab[letter].empty())
            {
                elem& e = tab[letter].front();
                int nextLetter = words[e.wordIndex][e.charIndex + 1] - 'a';
                if(nextLetter == - 'a') // this was the last char of this word
                    ret++;
                else if(nextLetter == letter) // push to the temporary list, which will be merged in the end of the loop
                    newList.emplace_front(e.wordIndex, e.charIndex + 1);
                else // push the the correct list
                    tab[nextLetter].emplace_front(e.wordIndex, e.charIndex + 1);
                tab[letter].pop_front();
            }
            tab[letter] = newList;
        }
        return ret;
    }
};
