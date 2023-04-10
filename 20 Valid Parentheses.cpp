class Solution {
public:
    bool isValid(string s) 
    {
        stack<char> st;
        st.push('$');
        for(char c : s)
        {
            if(c == '(' || c == '{' || c == '[')
                st.push(c);
            else
            {
                if(st.top() == '{' && c == '}' || st.top() == '(' && c == ')' || st.top() == '[' && c == ']')
                    st.pop();
                else
                    return false;
            }
        }
        if(st.size() > 1)
            return false;
        return true;
    }
};
