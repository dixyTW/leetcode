class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        source: https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/discuss/1424118/Python3-2-solutions-dp-and-bitset
        method 1: bitmap
        bitmap keeps track of all the possible sums that can be obtained by choosing 1 number from each row. After initializing the bitmap, we just need to calculate the min difference of every number thats stored in bitmap and return the smallest difference.
        """
        # largest = 4901 # 70*70 constraint
        # bitmap = 0b1
        # Min = float('inf')
        # for row in mat:
        #     temp = 0
        #     for num in row:
        #         temp |= bitmap << num
        #     bitmap = temp
        # for i in range(largest):
        #     if (bitmap >> i) & 1 == 1:
        #         Min = min(Min, abs(target-i))
        # return Min
        """
        method 2: DP
        
        """
        m, n = len(mat), len(mat[0])
        mn = [min(row) for row in mat]
        
        @cache 
        def fn(i, x): 
            """Return minimum absolute difference."""
            if i == m: return abs(x)
            if x <= 0: return fn(i+1, x-mn[i])
            ans = inf 
            for j in range(n): 
                ans = min(ans, fn(i+1, x-mat[i][j]))
            return ans 
        
        return fn(0, target)