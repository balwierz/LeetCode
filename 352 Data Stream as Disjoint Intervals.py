class SummaryRanges:

    def __init__(self):
        self.seen = set()
        self.intervals = set()    # tuples [beg, end]
        self.right = dict()       # right coordinate from root (left)
        self.parent = dict()

    def root(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def addNum(self, x: int) -> None:
        if x in self.seen: return
        self.seen.add(x)
        self.intervals.add((x,x))
        self.right[x] = x
        self.parent[x] = x
        if x+1 in self.seen:
            #rightRoot = root(x+1)
            self.intervals.remove((x,x))
            self.intervals.remove((x+1, self.right[x+1]))
            self.intervals.add((x, self.right[x+1]))
            self.parent[x+1] = x
            self.right[x] = self.right[x+1]
        if x-1 in self.seen:
            leftRoot = self.root(x-1)
            self.parent[x] = leftRoot
            self.intervals.remove((x, self.right[x]))
            self.intervals.remove((leftRoot, x-1))
            self.intervals.add((leftRoot, self.right[x]))
            self.right[leftRoot] = self.right[x]

    def getIntervals(self) -> List[List[int]]:
        return sorted(list(self.intervals))
        
