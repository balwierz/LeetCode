class Solution:
    def alertNames(self, name: List[str], time: List[str]) -> List[str]:
        n = len(name)
        def time2int(time):
            h, m = time.split(":")
            return int(h)*60 + int(m)
        data = defaultdict(list)
        for i in range(n):
            data[name[i]].append(time2int(time[i]))
        ret = []
        for name in sorted(data.keys()):
            if len(data[name]) < 3:
                continue
            data[name].sort()
            for i in range(2, len(data[name])):
                if data[name][i] - data[name][i-2] <= 60:
                    ret.append(name)
                    break
        return ret
