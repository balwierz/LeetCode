class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        X = defaultdict(list)
        for j, datum in enumerate(list(accumulate(arr, lambda a, b: a^b, initial=0))):
            X[datum].append(j) # = [j, X[datum][1] + 1, X[datum][2] + X[datum][1]*(j-X[datum][0]-1)]
        #print(X)
        ret = 0
        for arr in X.values():
            i = 0
            last = 1
            for drag, j in enumerate(arr):
                last += drag * (j - i) - 1
                #print("last", last)
                ret += last
                i = j
        return ret
