class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        result: TLE (accepted with lru_cache)
        brute force: try every option with dfs
        runtime: O(3^n), space: O(1) (without lru_cache, O(mn)#number of states, O(mn)) #disregarding string parsing
        """
        # @lru_cache(None) #speed up, effectively same thing as memoirzation
        # def dfs(w1, w2):
        #     if not w1 and not w2:
        #         return 0
        #     if not w1 or not w2:
        #         return len(w1) if len(w2) == 0 else len(w2)
        #     if w1[0] == w2[0]:
        #         return dfs(w1[1:], w2[1:])
        #     insert = 1 + dfs(w1, w2[1:])
        #     delete = 1 + dfs(w1[1:], w2)
        #     replace = 1 + dfs(w1[1:], w2[1:])
        #     return min(insert, delete, replace)
        # return dfs(word1, word2)
        """
        result: AC
        DP: bottom up build up of 2d array
        runtime: O(mn), space: O(mn)
        """
        mem = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for r in range(1, len(word1)+1):
            mem[r][0] = r
        for c in range(1, len(word2)+1):
            mem[0][c] = c
        for r in range(len(word1)):
            for c in range(len(word2)):
                if word1[r] == word2[c]:
                    mem[r+1][c+1] = mem[r][c]
                else:
                    mem[r+1][c+1] = min(mem[r][c+1], mem[r+1][c], mem[r][c]) + 1
        return mem[-1][-1] 
                    