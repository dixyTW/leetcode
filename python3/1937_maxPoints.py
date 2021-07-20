class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        result: TLE
        naive solution
        runtime: O(mn^2)
        """
        # mem = [[0 for _ in range(len(points[0]))] for _ in range(len(points)+1)]
        # for i in range(1, len(points)+1):
        #     for j in range(len(points[0])):
        #         for k in range(len(points[0])):
        #             mem[i][j] = max(mem[i][j], mem[i-1][k]-abs(j-k)+points[i-1][j])
        # return max(mem[-1])
        """
        source: https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/Python-3-DP-Explanation-with-pictures.
        """
        mem = [[0 for _ in range(len(points[0]))] for _ in range(len(points)+1)]
        for i in range(1, len(points)+1):
            left = [0 for _ in range(len(points[0]))]
            right = [0 for _ in range(len(points[0]))]
            prev = 0
            for j in range(len(points[0])):
                left[j] = max(prev-1, mem[i-1][j])
                prev = left[j]
            prev = 0
            for j in range(len(points[0])-1, -1, -1):
                right[j] = max(prev-1, mem[i-1][j])
                prev = right[j]
            for j in range(len(points[0])):
                mem[i][j] = max(left[j], right[j]) + points[i-1][j]
        return max(mem[-1])
        