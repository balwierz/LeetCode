class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
            if t == '+':
                stack.append(a+b)
            elif t == '-':
                stack.append(b-a)
            elif t == '*':
                stack.append(a*b)
            elif t == '/':
                s = -1 if b / a < 0 else 1
                stack.append(s * (abs(b)//abs(a)))
            else:
                stack.append(int(t))
        return stack.pop()
