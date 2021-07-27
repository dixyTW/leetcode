class Solution:
    def numDecodings(self, s: str) -> int:
        """
        result: TLE
        brute force dfs: slowly work through the string 
        runtime: O(2^n), space: O(n)
        """
#         dic = {str(i) for i in range(1,27)}
#         self.ans = 0
#         self.lst = []
#         def dfs(i):
#             if len(self.lst) == i:
#                 self.ans += 1
#                 return
#             if self.lst[i] == "0":
#                 return
#             if i+1 < len(self.lst) and self.lst[i] + self.lst[i+1] in dic:
#                 dfs(i+2)
#             dfs(i+1)
#         if not s:
#             return 0
#         for c in s:
#             self.lst.append(c)
#         dfs(0)
#         return self.ans
        """
        result: AC
        DP: advanced version of climb stairs
        runtime: O(n), space: O(n)
        """
        if s[0] == "0":
            return 0
        mem = [0 for _ in range(len(s)+1)]
        mem[0] = 1
        mem[1] = 1 
        for i in range(1, len(s)):
            if s[i] != "0":
                mem[i+1] += mem[i]
            if 10 <= int(s[i-1] + s[i]) <= 26:
                mem[i+1] += mem[i-1]
        return mem[-1]