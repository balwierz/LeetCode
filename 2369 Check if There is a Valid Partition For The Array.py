class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # state: num 1 previously (-1 means cut)
        #        isPossibleToCut at prev
        arr = [b-a for a,b in pairwise(nums)]
        #print(arr)
        oldStates = set([(-1, False)])
        for val in arr:
            if len(oldStates) == 0:
                return False
            newStates = set()
            #print(val, oldStates)
            for num1, isPossible in oldStates:
                if val == 0:
                    if num1 == 0:
                        newStates.add((0, True))
                    elif num1 == 1:
                        if isPossible:
                            newStates.add((0, False))
                    elif num1 == 2:  # it is always possible
                        # we must cut at current zero
                        newStates.add((-1, False))
                    else: # -1
                        newStates.add((0, False))
                elif val == 1:
                    if num1 == 0:
                        newStates.add((-1, False))
                        if isPossible:
                            newStates.add((1, False))
                    elif num1 == 1:
                        newStates.add((2, True))
                    elif num1 == 2:  # we have to cut at current 1
                        newStates.add((-1, False))
                    else:  # -1 cut
                        newStates.add((1, False))
                else:   # larger number we have to cut
                    if num1 == 0 or num1 == 2:
                        newStates.add((-1, False))
            oldStates = newStates
        #print(oldStates)
        for num1, isPossible in oldStates:
            if num1 in [0, 2]:
                return True
        return False

class Solution2:
    def validPartition(self, nums: List[int]) -> bool:
        # state: num 1 previously (-1 means cut)
        #        isPossibleToCut at prev
        arr = [b-a for a,b in pairwise(nums)]
        #print(arr)
        oldStates = set([(-1, False)])
        for val in arr:
            newStates = set()
            #print(val, oldStates)
            for num1, isPossible in oldStates:
                if val == 0:
                    if num1 == 0:
                        newStates.add((0, True))
                    elif num1 == 1:
                        if not isPossible:
                            pass
                        else:  # must cut on prev 1
                            newStates.add((0, False))
                    elif num1 == 2:  # it is always possible
                        # we must cut at current zero
                        newStates.add((-1, False))
                    else: # -1
                        newStates.add((0, False))
                elif val == 1:
                    if num1 == 0:
                        if not isPossible:
                            # we have to cut at current 1
                            newStates.add((-1, False))
                        else:
                            # we can cut at prev0 or at curr1
                            newStates.add((-1, False))
                            newStates.add((1, False))
                    elif num1 == 1:
                        newStates.add((2, True))
                    elif num1 == 2:  # we have to cut at current 1
                        newStates.add((-1, False))
                    else:  # -1 cut
                        newStates.add((1, False))
                else:   # larger number we have to cut
                    if num1 == -1:
                        pass
                    elif num1 == 0:
                        # we have to cut at current x
                        newStates.add((-1, False))
                    elif num1 == 1:
                        pass
                    else: # 2
                        newStates.add((-1, False))
            oldStates = newStates
        #print(oldStates)
        for num1, isPossible in oldStates:
            if num1 in [0, 2]:
                return True
        return False
        
