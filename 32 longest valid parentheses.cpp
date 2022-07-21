class Solution {
public:
    int longestValidParentheses(string s)
    {
        int ret = 0;
        stack<int> st;
        vector<int> matching(s.size(), -1);
        
        for(int i=0; i<s.size(); i++)
        {
            if(s[i] == '(')
                st.push(i);
            else // ')'
            {
                if(! st.empty())
                {
                    int last = st.top();
                    st.pop();
                    matching[i] = last;
                }
            }
        }
        
        int currMatching = 0;
        for(int j=s.size()-1; j>=0; j--)
        {
            if(matching[j] >= 0)
            {
                currMatching += j-matching[j]+1;
                j = matching[j];
                ret = max(ret, currMatching);
            }
            else
            {
                ret = max(ret, currMatching);
                currMatching = 0;
            }
        }
        
        return ret;
    }
    
    
    
    
    int foolongestValidParentheses(string s)
    {
        int ret = 0;
        stack<int> st;
        int prevValidStart = 100000;
        for(int i=0; i<s.size(); i++)
        {
            if(s[i] == '(')
                st.push(i);
            else // ')'
            {
                if(! st.empty())
                {
                    int last = st.top();
                    st.pop();
                    int thisValid = i-last+1;
                    if(last < prevValidStart)
                    { // () encompassing prevValid interval
                        prevValidStart = last;
                    }
                    else
                    { // () joining on equal level (...)()
                        thisValid = i-prevValidStart+1;
                    }
                    ret = max(ret, thisValid);
                }
                else
                {
                    prevValidStart = i+1;
                }
            }
        }
        return ret;
    }
};
