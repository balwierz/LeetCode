class Food
{
    public:
    int rating;
    string name;
    Food(const string &name, const int &rating) : rating(rating), name(name) {}
    bool operator<(const Food &other) const
    {
        if(rating == other.rating)
            return name > other.name;
        return rating < other.rating;
    }
};
class FoodRatings
{
    unordered_map<string, string> food2cui;
    unordered_map<string, set<Food>> cui2set;
    unordered_map<string, int> food2rating;
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings)
    {
        for(int i=0; i<foods.size(); ++i)
        {
            food2cui[foods[i]] = cuisines[i];
            auto &m = cui2set[cuisines[i]];
            m.emplace(foods[i], ratings[i]);
            food2rating[foods[i]] = ratings[i];
        }
    }
    
    void changeRating(string food, int newRating)
    {
        string &cui = food2cui[food];
        auto &m = cui2set[cui];
        int oldRating = food2rating[food];
        food2rating[food] = newRating;
        auto fIt = m.find(Food(food, oldRating));
        m.erase(fIt);
        m.emplace(food, newRating);
    }
    
    string highestRated(string cuisine)
    {
        auto &s = cui2set[cuisine];
        return s.rbegin()->name;
    }
};
