class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        tab = []
        n = len(board)
        for i in range(n):
            if i % 2:
                tab.extend(reversed(board[n-1-i]))
            else:
                tab.extend(board[n-1-i])
        n *= n
        #print(tab)
        state = set([0])
        tab[0] = -2  # visited
        step = 0
        while state:
            #print("step ", step, " ", state)
            newState = set()
            for pos in state:
                if pos == n-1:
                    return step;
                for jump in range(pos+1, min(n, pos+7)):
                    if tab[jump] > 0:
                        jump2 = tab[jump]-1
                        tab[jump] = -2
                        #print(jump, " ", tab[jump])
                        #if tab[jump2] != -2:
                        newState.add(jump2)
                        #print("by ladder ", jump2)
                    elif tab[jump] != -2:  # not processed
                        newState.add(jump)
                        tab[jump] = -2
                        #print("no ladder ", jump)
            state = newState
            step += 1
        return -1
