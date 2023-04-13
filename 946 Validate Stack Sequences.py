class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = [-1]
        n = len(pushed)
        a = 0
        b = 0
        while a<n or b<n:
            if b < n and st[-1] == popped[b]:
                st.pop()
                b += 1
            elif a < n:
                st.append(pushed[a])
                a += 1
            else:
                return False
        return True
