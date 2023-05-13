class Solution:
    def bestClosingTime(self, customers: str) -> int:
        nYright = sum(1 for c in customers if c=="Y")
        nNleft = 0
        customers += "N"
        best = float('inf')
        bestI = -1
        for i, x in enumerate(customers):
            score = nNleft + nYright
            if score < best:
                bestI = i
                best = score
            if x == "N":
                nNleft += 1
            else:
                nYright -= 1
        return bestI
