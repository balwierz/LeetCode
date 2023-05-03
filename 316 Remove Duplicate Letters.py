class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        If the character c is not in the stack,
        remove all chars from the stack that are greater than c and appear later in the input string.

        This is because we want to keep the smallest lexicographical order.
        We will keep removing characters until either the stack is empty or the top element of the stack is less than or equal to c.
        """
        stack = []
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)

        return "".join(stack)


class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        s = [ord(x)-ord('a') for x in s]  # now s is an array of numbers
        missingLetters = sorted(Counter(s).keys())
        #print(missingLetters)
        missingMask = 0
        for x in missingLetters:
            missingMask |= (1 << x)
        #print(missingMask)
        n = len(s)
        mask = [0] * n
        runMask = 0
        for i in range(n-1, -1, -1):
            runMask |= (1 << s[i])
            mask[i] = runMask
        #print(mask)
        def tryLetter(letter, startIndex, missingMask):
            for i in range(startIndex, n):
                if s[i] == letter:   # the first letter
                    if missingMask & mask[i] == missingMask:  # all letters accounted for
                        return i
                    return -1 # at first letter there are not enough letters following
            return -1  # no letter found at all
        
        ret = []
        thisPos = 0
        while missingMask:   # still letters to be found
            # try all letters
            for letter in range(26):
                if missingMask & (1 << letter):
                    #print("trying letter ", letter, " at position ", thisPos, "with mask ", missingMask)
                    a = tryLetter(letter, thisPos, missingMask)
                    if a == -1:
                        # this letter did not work
                        #print("  it did not work")
                        continue  # continue with next letter
                    # it worked
                    #print("  it worked, the result is position ", a)
                    ret.append(letter)
                    thisPos = a+1
                    missingMask &= ~(1 << letter)
                    break
        #print("the result is ", ret)
        return ''.join(chr(x+ord('a')) for x in ret)


