vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2)
{
    vector<vector<int>> ret;
    auto a = nums1.begin();
    auto b = nums2.begin();
    while(a != nums1.end() || b != nums2.end())
    {
        int av = 2000, bv = 2000, sum = 0;
        if(a != nums1.end())
            av = (*a)[0];
        if(b != nums2.end())
            bv = (*b)[0];
        int m = min(av, bv);  // new id
        if(av == m)
            sum += (*a++)[1];
        if(bv == m)
            sum += (*b++)[1];
        ret.push_back(vector<int>{m, sum});
    }
    return ret;
}
