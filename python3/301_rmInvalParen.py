class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        bfs: check all substrings and return the longest valid parenthesis string list
        """
        def is_valid(s):
            nOpen = 0
            for i, c in enumerate(s):
                if c == "(":
                    nOpen += 1
                elif c == ")":
                    if nOpen == 0:
                        return False
                    else:
                        nOpen -= 1
            return nOpen == 0
        
        q = deque([s])
        validStrLst = []
        visited = set()

        while q:
            M = len(q)
            for _ in range(M):
                cur = q.popleft()
                if is_valid(cur):
                    validStrLst.append(cur)
                for i, c in enumerate(cur):
                    if c == "(" or c == ")":
                        newStr = cur[:i] + cur[i+1:]
                        if newStr not in visited:
                            q.append(newStr)
                            visited.add(newStr)
                        
            if validStrLst:
                return validStrLst
        
        
        
        """
        dfs check every valid parentheses and return the longest valid parentheses
        """
#         N = len(s)
#         @lru_cache(None)
#         def helper(i, nOpen):
#             """
#             returns set of valid parentheses 
#             nOpen: current number of open parenthesis
#             """
#             ans = set()
#             if nOpen < 0:
#                 return ans
#             if i == N:
#                 if nOpen == 0:
#                     ans.add("")
#                 return ans
            
#             # can't skip alphabets
#             if s[i] == '(' or s[i] == ')':
#                 ans.update(helper(i+1, nOpen))
            
#             if s[i] == '(':
#                 nOpen += 1
#             elif s[i] == ')':
#                 nOpen -= 1
#             for suffix in helper(i+1, nOpen):
#                 ans.add(s[i]+suffix)
#             return ans
            
#         validParens = helper(0, 0)
#         maxlen = max(map(len, validParens))
#         return filter(lambda x: len(x) == maxlen, validParens)