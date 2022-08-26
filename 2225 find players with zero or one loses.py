class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        plLoses = dict()
        for i in range(len(matches)):
            winner, loser = matches[i]
            if not (winner in plLoses):
                plLoses[winner] = 0
            if loser in plLoses:
                plLoses[loser] += 1
            else:
                plLoses[loser] = 1
        ret0 = [i for i in plLoses if plLoses[i] == 0]
        ret1 = [i for i in plLoses if plLoses[i] == 1]
        return [sorted(ret0), sorted(ret1)]
