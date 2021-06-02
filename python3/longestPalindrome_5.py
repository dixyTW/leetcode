class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        result: TLE
        naive solution: checking every substring if its a palindrome
        runtime: O(n^3), space: O(1)
        """
#         def is_pal(l, r) -> bool:
#             #helper function that checks if a string is a palindrome
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True
        
#         Max = 0
#         start = 0
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 if is_pal(i, j):
#                     if j - i + 1 > Max:
#                         start, Max = i, j - i + 1
#         return s[start:start+Max] 
        
        """
        result: Accepted
        DP solution: construct 2D graph where dp[i][j] means s[i:j]
        to check if a string is a palindrome
        dp[i][j] = True if dp[i+1][j-1] and s[i] == s[j]
        In order to use this pattern, we need to construct the dictionary in a way that utilizes previous results
        runtime: O(n^2), space: O(len(s)^2)
        """
        
#         mem = [[False for _ in range(len(s))] for _ in range(len(s))]
#         start = 0
#         Max = 0
#         for i in range(len(s)-1, -1, -1):
#             for j in range(i, len(s)):
#                 mem[i][j] = s[i] == s[j] and (j - i <= 1 or mem[i+1][j-1]) #swaping and statement determines if the solution gets accepted or not
#                 if mem[i][j] and j-i+1 > Max:
#                     start = i
#                     Max = j-i+1
#         return s[start:start+Max]

        """
        result: Accepted
        improved naive solution: 
        traverse the string, each index acts as a pivot (middle point) of a word
        we start at each index, and expand both ways to check if the string is still
        a palindrome or not
        runtime: O(n^2), space: O(1)
        """
        self.max, self.start = 1, 0
        def helper(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > self.max:
                self.max = r - l - 1
                self.start = l + 1
        for i in range(len(s)-1):
            helper(i, i)
            helper(i, i+1)
        return s[self.start:self.start+self.max]