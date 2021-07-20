class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        result: TLE
        naive: locate the lowest height, use that as the height of the rectangle and calculate its area, divide the heights into half based on the lowest height and repeat
        runtime: O(n^2), space: O(1)
        """
#         self.ans = 0
#         def helper(l, r):
#             if l >= r:
#                 return
#             else:
#                 Min = float('inf')
#                 split_index = -1
#                 for i in range(l, r):
#                     if heights[i] < Min:
#                         Min = heights[i]
#                         split_index = i
#                 width, height = r - l, Min
#                 self.ans = max(self.ans, width*height)
#                 helper(l, split_index)
#                 helper(split_index+1, r)
#         helper(0, len(heights))
#         return self.ans
        """
        monotonic stack
        """
        stack = [-1]
        heights.append(0)
        ans = 0
        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()] 
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        heights.pop()
        return ans
        