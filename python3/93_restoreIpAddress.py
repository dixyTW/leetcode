class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        result: AC
        dfs: using lists instead of string just made this more complicated, implementation wise and time complexity
        """
#         self.ans = []
#         def helper(lst,cur,i):
#             if len(lst) == 3 and cur and int("".join(cur)) <= 255 and i == len(s):
#                 lst.append("".join(cur))
#                 self.ans.append(".".join(lst))
#                 return
#             if i >= len(s) or i >= 12:
#                 return
#             else:
#                 if len(cur) > 0 and int("".join(cur)) <= 255:
#                     helper(lst+["".join(cur)], [], i)
#                 if len(cur) < 3:
#                     if len(cur) > 0 and cur[0] == "0":
#                         return
#                     else:
#                         helper(lst, cur+[s[i]], i+1)
                
#         helper([], [], 0)
#         return self.ans
            
        """
        result: AC
        Clean DFS
        runtime: O(3^n) without considering string operations
        """
        self.ans = []
        def helper(lst, s):
            if len(lst) > 4:
                return
            if len(lst) == 4 and not s:
                self.ans.append(".".join(lst))
            for i in range(1, min(len(s)+1, 4)):
                if s[:i] == "0" or (s[0] != "0" and int(s[:i]) <= 255):
                    helper(lst + [s[:i]], s[i:])
        helper([],s)
        return self.ans
            