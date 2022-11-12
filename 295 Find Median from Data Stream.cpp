class MedianFinder {
    int nRight;
    int nLeft;
    priority_queue<int, vector<int>> leftHeap;
    priority_queue<int, vector<int>, greater<int>> rightHeap;
public:
    MedianFinder()
    {
        nRight = 0;
        nLeft = 0;
        leftHeap.push(INT_MIN);
        rightHeap.push(INT_MAX);
    }
    
    void addNum(int num)
    {
        // choose heap:
        if(num <= leftHeap.top())
        {
            leftHeap.push(num);
            nLeft ++;
        }
        else
        {
            rightHeap.push(num);
            nRight ++;
        }
        if(nLeft == nRight + 2)
        {
            int elem = leftHeap.top();
            leftHeap.pop();
            rightHeap.push(elem);
            nLeft--;
            nRight++;
        }
        if(nRight == nLeft + 1)
        {
            int elem = rightHeap.top();
            rightHeap.pop();
            leftHeap.push(elem);
            nLeft++;
            nRight--;
        }
    }
    
    double findMedian()
    {
        if(nRight == nLeft)
            return (leftHeap.top() + rightHeap.top()) / 2.0;
        return leftHeap.top();
    }
};
