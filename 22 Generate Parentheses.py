class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        data = [set() for _ in range(n+1)]
        data[0] = set([""])
        for i in range(1, n+1):
            for conf in data[i-1]:
                data[i].add("(" + conf + ")")
            for j in range(1, i):
                k = i-j
                for confL in data[j]:
                    for confR in data[k]:
                        data[i].add(confL + confR)
        return list(data[n])
