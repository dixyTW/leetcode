class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        source: https://leetcode.com/problems/painting-a-grid-with-three-different-colors/discuss/1330185/C%2B%2BPython-DP-and-DFS-and-Bitmask-Picture-explain-Clean-and-Concise
        result: accepted
        dfs+memorization+bitmask solution: For each layer, we want to determine all possible patterns without having two adjacent cells having the same color.
        generating mask patterns and traversing each layer given a mask is optimized by storing result in a cache (memoirzation)
        using bitmask instead of actual strings to get a valid pattern to reduce runtime
        runtime: O(N * 3^M * 2^M), space: O(N * 3^M + 3^M * 2^M)
        """
        def get_color(mask, pos):
            return (mask >> 2*pos) & 3
        
        def set_color(curMask, color, pos):
            #set bitmask color (representing each color with 2 bits)
            return curMask | (color << 2*pos)
            
        def generatePatterns(prevMask,curMask,pos,lst):
            if pos == m:
                lst.append(curMask)
                return
            for c in [1,2,3]:
                if c != get_color(prevMask, pos) and (pos == 0 or get_color(curMask, pos-1) != c):
                    generatePatterns(prevMask, set_color(curMask, c, pos), pos+1, lst)
        
        @lru_cache(None)
        def dp(mask, level):
            if level == n:
                return 1
            ans = 0
            for pat in findPattern(mask):
                ans += dp(pat, level+1)
            return ans
            
        @lru_cache(None)
        def findPattern(mask):
            #finds list of patterns given the depending on the previous layer
            lst = []
            generatePatterns(mask, 0, 0, lst)
            return lst
            

        return dp(0, 0) % (10**9 + 7)