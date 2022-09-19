class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        playerN = len(players)
        trainers = sorted(trainers)
        trainerN = len(trainers)
        tI = 0
        ret = 0
        for p in players:
            while tI < trainerN and trainers[tI] < p:
                tI += 1
            if tI == trainerN:
                break;
            ret += 1
            tI += 1
        return ret
