    def frequencySort(self, s: str) -> str:
        ret = ""
        for k, v in sorted(Counter(s).items(), key=lambda x : x[1], reverse=True): ret += k * v
        return ret
