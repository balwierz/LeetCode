class Solution:
    def maximumLength(self, s: str) -> int:
        ret = -1
        data = sorted([(len(list(group)), key) for key, group in groupby(s)], reverse=True)
        longest = data[0][0]
        seen = defaultdict(set)  # len key, set is letters
        for numRuns, (runLen, letter) in [(len(list(group)), key) for key, group in groupby(data)]:
            if longest - runLen >= 2:
                break
            if numRuns >= 3:
                return runLen
            if numRuns == 2 and runLen >= 3:
                ret = max(ret, runLen - 1)
            seen[runLen].add(letter)
            if letter in seen[runLen+1]:
                ret = max(ret, runLen)
            if runLen >= 3:
                ret = max(ret, runLen-2)
        return ret
