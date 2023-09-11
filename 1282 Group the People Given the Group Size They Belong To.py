class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        data = [[] for _ in range(501)]                                       
        ret = []
        for i, e in enumerate(groupSizes):
            data[e].append(i)
            if len(data[e]) == e:
                ret.append(data[e])
                data[e] = []
        return ret
