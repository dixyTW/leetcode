class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        result: TLE
        brute force: form all subsequence of length t using s and compare
        runtime: O(s!), space: O(1)
        """
#         def helper(str1, i):
            
#             if str1 == t:
#                 return 1
#             if len(str1) == len(t):
#                 return 0 
#             ans = 0
#             for j in range(i, len(s)):
#                 ans += helper(str1+s[j], j+1)
#             return ans
#         return helper("", 0)
        """
        result: AC
        DP:
        runtime: O(s*t), space: O(s*t)
        """
        mem = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            mem[0][i] = 1
        for i in range(len(t)):
            for j in range(len(s)):
                mem[i+1][j+1] = (mem[i+1][j] + mem[i][j]) if t[i] == s[j] else mem[i+1][j]
        return mem[-1][-1]
        
    