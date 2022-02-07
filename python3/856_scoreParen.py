class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                tmp = stack.pop()
                if tmp == 0:
                    ans = 1
                else:
                    ans = 2*tmp
                if stack:
                    stack[-1] += ans
                else:
                    stack.append(ans)
        return stack[-1]