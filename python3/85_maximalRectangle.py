class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        result: AC
        binary string solution: https://leetcode.com/problems/maximal-rectangle/discuss/1349824/Python-Binary-string-Solution-O(N3)
        runtime: O(n^3), space: O(n)
        """
        # def helper(i):
        #     #gets the longest consecutive 1s in a binary
        #     max_len = 0
        #     count = 0
        #     while i != 0:
        #         if i & 1:
        #             count += 1
        #         else:
        #             max_len = max(max_len, count)
        #             count = 0
        #         i = i >> 1
        #     max_len = max(max_len, count)
        #     return max_len
        # if not matrix:
        #     return 0
        # area = 0
        # lst = [0 for _ in range(len(matrix[0]))]
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] == "1":
        #             lst[c] += 2**r
        # for i in range(len(lst)):
        #     b = lst[i]
        #     for j in range(i, len(lst)):
        #         b &= lst[j]
        #         height = helper(b)
        #         width = j-i+1
        #         area = max(area, height*width)
        # return area
        
        """
        result: AC
        Monotonic stack
        runtime: O(n^2), space: O(n)
        """
        def helper(heights):
            #uses monotonic stack to calculate max area
            stack = [-1]
            heights.append(0)
            area = 0 
            for i, h in enumerate(heights):
                while h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    area = max(height*width, area)
                stack.append(i)
            heights.pop()
            return area
        if not matrix:
            return 0
        max_area = 0
        lst = [0 for _ in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    lst[c] += 1
                else:
                    lst[c] = 0
            max_area = max(max_area, helper(lst))
        return max_area