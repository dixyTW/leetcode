class Solution:
    def calculate(self, s: str) -> int:
        def update(op, n):
            if op == "+":
                stack.append(n)
            if op == "-":
                stack.append(0 - int(n))
            
        num, sign, stack, i = 0, "+", [], 0
        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] == "(":
                j, num = self.calculate(s[i+1:])
                i += j
            elif s[i] == ")":
                update(sign, num)
                return i+1, sum(stack) 
            elif s[i] in "+-*/":
                #operational char
                update(sign, num)
                num, sign = 0, s[i]
            i += 1
        update(sign, num)
        return sum(stack)