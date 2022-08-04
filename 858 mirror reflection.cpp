// could be solved in terms of LCM/p and LCM/q
class Solution {
public:
    int mirrorReflection(int p, int q)
    {
        int side = 0; // left
        int direction = 0; // up
        int a = 0; // from the corner
        while(true)
        {
            int m = (p-a) % q; // how much is missing to the top
            if(m == 0)  // we hit a detector
            {
                if(direction == 0)  // 1 or 2
                {
                    if(((p-a) / q) % 2 == 0)  // same side
                    {
                        if(side == 0)
                            return 2;
                        else
                            return 1;
                    }
                    else // different side
                    {
                        if(side == 0)
                            return 1;
                        else
                            return 2;
                    }
                }
                else // direction = 1 downwards
                    return 0;
                
            }
            side = ((p-a) / q) % 2 ? 1-side : side;
            direction = 1 - direction; // flip
            a = q - m;

        }
    }
};
