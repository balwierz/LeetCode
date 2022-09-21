class Date:
    def __init__(self, monthLen = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]):
        self.cumDays = tuple(accumulate(monthLen))
    def date2days(self, date: str):
        monS, dayS = date.split("-")
        return self.cumDays[int(monS)-1] + int(dayS)
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        date = Date()
        maxArrive = max(date.date2days(arriveAlice), date.date2days(arriveBob))
        minLeave  = min(date.date2days(leaveAlice), date.date2days(leaveBob))
        return max(0, minLeave - maxArrive + 1)
