class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(None)
        def is_pal(i,j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return is_pal(i+1, j-1)
        
        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return 0
            ans = float('inf')
            for j in range(i,len(s)):
                if is_pal(i,j):
                    ans = min(ans, 1+dp(j+1))
            return ans
        return dp(0) - 1 
            
        
        
        # mem = [[float('inf') for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)-1, -1, -1):
        #     for j in range(i, len(s)):
        #         if j - i <= 1:
        #             mem[i][j] = int(not s[i] == s[j])
        #         elif s[i] == s[j] and mem[i+1][j-1] == 0:
        #             mem[i][j] = 0
        #         else:
        #             for k in range(i, j):
        #                 mem[i][j] = min(mem[i][j], mem[i][k] + mem[k+1][j] + 1)
        # return mem[0][len(s)-1]
        
#     def minCut(self, s: str) -> int:
#         if self.is_pal(s):
#             return 0
#         ans = float('inf')
#         for i in range(1,len(s)):
#             ans = min(self.minCut(s[:i])+self.minCut(s[i:])+1, ans)
#         return ans
        
#     def is_pal(self,string):
#         leng = len(string)
#         for i in range(leng//2):
#             if string[i] != string[leng-1-i]:
#                 return False
#         return True