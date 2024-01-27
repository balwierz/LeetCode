class Solution:
    def minimumPushes(self, word: str) -> int:
        return [0, 8, 24, 48][len(word)//8] + (len(word)//8+1) * (len(word) % 8)
