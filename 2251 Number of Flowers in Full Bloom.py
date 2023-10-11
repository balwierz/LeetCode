class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        data = []
        for a, b in flowers:
            data.append((b+1, -2))
            data.append((a, -1))
        for i, p in enumerate(people):
            data.append((p, i))
        lvl = 0
        ret = [0] * len(people)
        for p, idx in sorted(data):
            if idx >= 0:
                ret[idx] = lvl
            else:
                if idx == -1:
                    lvl += 1
                else:
                    lvl -= 1
        return ret


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start, end = sorted([start for start,_ in flowers]), sorted([end for _,end in flowers])
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]
            
