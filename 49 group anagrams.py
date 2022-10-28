class Solution:
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        def str2vec(s):
            ret = 0
            for a in s:
                ret += 1 << ((ord(a) - ord('a')) * 8)
            return ret
        d = defaultdict(list)
        for s in strs:
            d[str2vec(s)].append(s)
        return d.values()
    
    def groupAnagrams(self, strs):
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [list(members) for _, members in groups]
