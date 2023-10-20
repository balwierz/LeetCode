# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def flatten(self, data):
        if isinstance(data, list):
            ret = []
            for x in data:
                ret.extend(self.flatten(x))
            return ret
        if data.isInteger():
            return [data.getInteger()]
        return self.flatten(data.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.data = self.flatten(nestedList)
        self.i = -1
        
    def next(self) -> int:
        self.i += 1
        return(self.data[self.i])

    def hasNext(self) -> bool:
        return self.i < len(self.data)-1
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
