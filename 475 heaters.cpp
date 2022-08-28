class Solution {
    struct elemT
    {
        int pos;
        char type;  // U; house, E: heater
        elemT(int pos, char type) : pos(pos), type(type) {}
        elemT() {}
        bool operator<(const elemT &other)
        {
            return pos < other.pos;
        }
    };
public:
    int findRadius(vector<int>& huus, vector<int>& heat)
    {
        int es = heat.size();
        int us = huus.size();
        sort(huus.begin(), huus.end());
        sort(heat.begin(), heat.end());
        // edges:
        int bestRadius = 0;
        if(huus[0] < heat[0])
            bestRadius = heat[0] - huus[0];
        if(heat[es-1] < huus[us-1])
            bestRadius = max(bestRadius, huus[us-1] - heat[es-1]);
        // convert into elemT:
        vector<elemT> huusElem(us);
        vector<elemT> heatElem(es);
        for(int i=0; i<us; i++)
            huusElem[i] = elemT(huus[i], 'U');
        for(int i=0; i<es; i++)
            heatElem[i] = elemT(heat[i], 'E');
        // merge them
        vector<elemT> tab(us+es);
        merge(huusElem.begin(), huusElem.end(), heatElem.begin(), heatElem.end(),
              tab.begin());
        // go to the first heater:
        int i = 0;
        while(tab[i].type=='U')
            i++;
        // the main loop:
        
        for(int heaterI = 0 ; heaterI < es-1; heaterI++)
        {
            int j=i+1;
            while(tab[j].type=='U')
                j++;
            // now i and j point to neighbouring heaters
            for(int k=i+1; k<j; k++)
                bestRadius = max(bestRadius, 
                                 min(tab[k].pos - tab[i].pos,
                                     tab[j].pos - tab[k].pos));
            i = j;
        }
        return bestRadius;
    }
};
