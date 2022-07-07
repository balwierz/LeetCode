class Solution {
public:
    string removeDigit(string number, char digit) 
    {
        auto it = number.begin();
        auto previt = it;
        for(;it<number.end();)
        {
            //cout << "a" << *it << ' ' << *previt << endl;
            while(it != number.end() && *it != digit)
                it++;
            if(it == number.end())
            {
                //cout << "c";
                number.erase(previt); return(number);
            }
            // pass all the identical chareacters to digit:
            while(*it == digit)
                it++;
            it--; // we are at the last character equal to digit
            if(it+1 == number.end())
            {
                number.erase(it); return(number);
            }
            if(*(it+1) > digit)
            {
                number.erase(it); return(number);
            }
            else
            {
                //cout << "b";
                previt = it;
                it++;
            }
        }
        number.erase(previt); return(number);
    }
};
