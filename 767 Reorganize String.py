class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        if (len(s)+1) // 2 < max(c.values()):
            return ""
        ret = [' '] * len(s)
        data = list(c.items()) #sorted(c.items(), key=lambda e: -e[1])
        maxI = 0
        for i, [letter, count] in enumerate(data):
            if count > data[maxI][1]:
                maxI = i
        data[0], data[maxI] = data[maxI], data[0]
        w = ""
        for letter, count in data:
            w += letter * count
        ret[::2] = w[:(len(w)+1)//2]
        ret[1::2] = w[(len(w)+1)//2:]
        return ''.join(ret
