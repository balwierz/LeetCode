class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word2multBak = {}
        nWrongBak = 0
        for word in words:
            if not word in word2multBak:
                nWrongBak += 1
                word2multBak[word] = 0
            word2multBak[word] -= 1
        k = len(words[0])
        n = len(s)
        z = len(words)
        ret = []
        for offset in range(k):   # loops modulo k
            nWrong = nWrongBak
            word2mult = (word2multBak).copy()
            for i in range(offset, n-k+1, k):
                w = s[i:i+k]
                if w in word2mult:
                    word2mult[w] += 1
                    if   word2mult[w] == 0:   nWrong -= 1
                    elif word2mult[w] == 1:   nWrong += 1
                # remove from the left
                if i-(z)*k >= 0:
                    w = s[i-(z)*k:i-(z-1)*k]
                    if w in word2mult:
                        word2mult[w] -= 1
                        if   word2mult[w] ==  0:  nWrong -= 1
                        elif word2mult[w] == -1:  nWrong += 1
                # check if we just found a match
                if nWrong == 0:
                    ret.append(i-(z-1)*k)
        return ret
