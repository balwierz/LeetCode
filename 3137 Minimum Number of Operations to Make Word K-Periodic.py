class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        return len(word)//k - Counter(word[i:i+k] for i in range(0,len(word),k)).most_common(1)[0][1]
