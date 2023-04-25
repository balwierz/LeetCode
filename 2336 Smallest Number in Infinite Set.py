class SmallestInfiniteSet:

    def __init__(self):
        self.lowest = 1
        self.arr = [True] * 1001
        

    def popSmallest(self) -> int:
        ret = self.lowest
        self.arr[self.lowest] = False
        while self.lowest <= 1000 and not self.arr[self.lowest]:
            self.lowest += 1
        return ret
        
    def addBack(self, num: int) -> None:
        self.arr[num] = True
        self.lowest = min(self.lowest, num)
        
