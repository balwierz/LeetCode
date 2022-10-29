class Flower
{
    public:
    int plantTime;
    int growTime;
    bool operator<(const Flower& other)
    {
        return growTime < other.growTime;
    }
    Flower(int plantTime, int growTime) : plantTime(plantTime), growTime(growTime) {}
    Flower() {}
};

class Solution 
{
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime)
    {
        int n = plantTime.size();
        vector<Flower> flowers(n);
        for(int i=0; i<n; i++)
            flowers[i] = Flower(plantTime[i], growTime[i]);
        sort(flowers.rbegin(), flowers.rend());
        int lastPlant = -1;
        int latestBloom = -1;
        for(int i=0; i<n; i++)
        {
            lastPlant += flowers[i].plantTime;
            latestBloom = max(latestBloom, lastPlant + flowers[i].growTime + 1);
        }
        return latestBloom;
    }
};
