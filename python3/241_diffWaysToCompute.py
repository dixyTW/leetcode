class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        if expression.isdigit():
            return [int(expression)]
        for i, e in enumerate(expression):
            if not e.isdigit():
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if e == "+":
                            ans.append(l+r)
                        elif e == "-":
                            ans.append(l-r)
                        else:
                            ans.append(l*r)
        
        return ans