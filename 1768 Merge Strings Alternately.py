class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([x if x else '' for d in zip_longest(word1, word2) for x in d])
