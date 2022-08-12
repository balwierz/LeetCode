class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        whenPossible = {}
        ret = 0
        t = 0
        for task in tasks:
            when = max(whenPossible.get(task, t), t)
            ret += when - t + 1
            t = when + 1
            whenPossible[task] = t + space
        return ret
