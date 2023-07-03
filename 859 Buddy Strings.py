class Solution:
    def buddyStrings(self, s: str, g: str) -> bool:
        if len(s) != len(g):
            return False
        diffs = []
        hasTwice = False
        seen = set()
        for i, [a, b] in enumerate(zip(s,g)):
            if a != b:
                diffs.append(i)
            if a in seen:
                hasTwice = True
            seen.add(a)
        if len(diffs) == 0 and hasTwice:
            return True
        if len(diffs) == 2 and s[diffs[0]] == g[diffs[1]] and s[diffs[1]] == g[diffs[0]]:
            return True
        return False
