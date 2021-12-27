class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        find longest palindrome substring starting from index 0
        """
        end = 1
        i = 1 #length of substring
        while i <= len(s):
            if i % 2:
                if s[:i//2 + 1] == s[i//2:i][::-1] and i > end:
                    end = i
            else:
                if s[:i//2] == s[i//2:i][::-1] and i > end:
                    end = i
            i += 1
        return s[end:][::-1] + s
        
        