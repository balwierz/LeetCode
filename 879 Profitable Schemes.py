class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        data = [[0] * (minProfit+1) for _ in range(n+1)]  # [people used][profit]
        data[0][0] = 1
        for nPeople, money in zip(group, profit):
            for startPeople in range(n-nPeople, -1, -1):
                thisPeople = startPeople + nPeople
                for startProfit in range(minProfit, -1, -1):
                    thisProfit = min(startProfit+money, minProfit)
                    data[thisPeople][thisProfit] += data[startPeople][startProfit]
                    data[thisPeople][thisProfit] %= 1_000_000_007
        return sum(data[i][minProfit] for i in range(n+1)) % 1_000_000_007
