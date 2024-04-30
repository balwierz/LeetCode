import numpy as np
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        state = [0] * 10  #np.array([0] * 10, dtype=int)
        data = np.zeros(shape=(2,2,2,2,2,  2,2,2,2,2), dtype=int)
        data[tuple(state)] = 1
        ret = 0
        for letter in word:
            dimI = ord(letter) - ord('a')
            state[dimI] = 1 - state[dimI]
            ret += data.item(*state)
            for dimJ in range(10):
                state[dimJ] = 1 - state[dimJ]
                ret += data.item(*state)
                state[dimJ] = 1 - state[dimJ]
            data[tuple(state)] += 1
        return ret
