class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        source: https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration
        result: accepted
        DP solution:
        Construct 2D array to save previous calculations
        Initiazlize extra row 0 for future calculation purposes (the proceeding for loops have some True values to base on)
        If string p starts with asterics, we initialize those values to true as well
        Pattern 1: If p[j] == "*", mem[i][j] remains true if mem[i-1][j], mem[i][j-1], or mem[i-1][j-1] is true. Appending a asteric to the string doesn't change the 
        Pattern 2: If p[j] is anything else but "*", we compare the current two chars s[i] and p[j]
        runtime: O(s*p), space: O(s*p)
        
        """
        mem = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        mem[0][0] = True
        for i in range(len(p)):
            if p[i] == "*":
                mem[0][i+1] = True
            else: 
                break
        for i in range(len(s)):
            for j in range(len(p)):
                
                if p[j] == "*":
                    mem[i+1][j+1] = mem[i][j] or mem[i][j+1] or mem[i+1][j]
                else:
                    mem[i+1][j+1] = mem[i][j] and (s[i] == p[j] or p[j] == "?")    
        return mem[-1][-1]