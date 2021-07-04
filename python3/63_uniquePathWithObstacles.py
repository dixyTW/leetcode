class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        result: accepted
        dp solution: modify the unique path I solution
        runtime: O(nm), space: O(mn) 
        """
        mem = [[0 for _ in range(len(obstacleGrid[0])+1)] for _ in range(len(obstacleGrid)+1)]
        mem[0][1] = 1
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] != 1:
                    mem[r+1][c+1] = mem[r][c+1] + mem[r+1][c]
        return mem[-1][-1]