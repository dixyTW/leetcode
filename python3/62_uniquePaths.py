class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        result: TLE
        naive solution: recursively compute all paths
        runtime: O(2^mn), O(1)
        """
        # self.ans = 0
        # def helper(r, c):
        #     if r < 0 or c < 0:
        #         return 
        #     if r == 0 and c == 0:
        #         self.ans += 1
        #         return
        #     helper(r-1, c)
        #     helper(r, c-1)
        # helper(m-1,n-1)
        # return self.ans 
        
        """
        result: accepted
        dp solution: construct dp array and calcuate unique paths bottom up
        runtime: O(mn), space: O(mn)
        """
        # mem = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # mem[0][1] = 1 #doesn't matter if its mem[1][0] or mem[0][1]
        # for r in range(1, n+1):
        #     for c in range(1, m+1):
        #         mem[r][c] = mem[r-1][c] + mem[r][c-1]
        # return mem[-1][-1]
        
        """
        result: accepted
        math solution: m+n choices, m times has to be downwards and n times has to be right
        runtime: O(m+n), space: O(1)
        """
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))