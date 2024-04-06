def minRemoveToMakeValid(self, s: str) -> str:
    fn = defaultdict(int, {"(":1, ")":-1})
    data    = list(accumulate([ fn[x] for x in s      ], lambda a, b: max(a, 0) +b))
    dataRev = list(accumulate([-fn[x] for x in s[::-1]], lambda a, b: max(a, 0) +b))[::-1]
    return "".join([s[i] for i in range(len(s)) if data[i] >= 0 and dataRev[i] >= 0])
