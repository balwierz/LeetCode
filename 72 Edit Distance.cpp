int minDistance(string w1, string w2) 
{
    int m = w1.size();
    int n = w2.size();
    w1 = "$" + w1;
    w2 = "$" + w2;
    vector<int> tab(m+1);
    for(int j=0; j<=m; j++)
        tab[j] = j;
    for(int i=1; i<=n; i++)
    {
        tab[0] = i;
        int last = i - 1;
        for(int j=1; j<=m; j++)
        {
            int match = last + (w1[j] == w2[i] ? 0 : 1);
            int insertion = tab[j] + 1;
            int deletion = tab[j-1] + 1;
            last = tab[j];
            tab[j] = min(match, min(insertion, deletion));
        }
    }
    return tab[m];
}
