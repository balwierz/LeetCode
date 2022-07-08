class Solution {
public:
    int maxArea(vector<int>& height) 
    {
        int i=0, j=height.size()-1;
        int maxVol = (j-i)*min(height[i], height[j]);
        while(i<j)
        {
            if(height[i] < height[j])
            {
                int old = height[i];
                while(i<j && old >= height[i])
                    i++;
                int thisVol = (j-i)*min(height[i], height[j]);
                if(thisVol > maxVol)
                    maxVol = thisVol;
            }
            else
            {
                int old = height[j];
                while(i<j && old >= height[j])
                    j--;
                int thisVol = (j-i)*min(height[i], height[j]);
                if(thisVol > maxVol)
                    maxVol = thisVol;
            }
        }
        return maxVol;
    }
};
