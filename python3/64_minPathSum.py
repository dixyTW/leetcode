class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        result: accepted
        dp solution: initialize the mem grid properly and follow the pattern below
        runtime: O(mn), space: O(mn)
        """
        mem = [[float('inf') for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)] #setting to every value to infinity so the first col and row retrieves the right value
        mem[0][1] = 0 #setting 0 for the first block mem[1][1] to initialize
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                mem[r+1][c+1] = min(mem[r+1][c], mem[r][c+1]) + grid[r][c]
        return mem[-1][-1]