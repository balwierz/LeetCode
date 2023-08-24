class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        rem = maxWidth-len(words[0])
        line = [words[0]]
        for w in words[1:]:
            if 1+len(w) > rem: # not the last line, print out
                txt = line[0]
                if len(line) == 1:
                    txt = txt.ljust(maxWidth)
                else:
                    shorterLen, numLonger = divmod(rem, len(line)-1) 
                    for x in line[1:]:
                        txt += " " * (shorterLen+1+(numLonger>0)) + x
                        numLonger -= 1
                line = [w]
                rem = maxWidth - len(w)
                ret.append(txt)
            else:
                line.append(w)
                rem -= len(w) + 1
        # last line:
        ret.append(' '.join(line).ljust(maxWidth))
        return ret
