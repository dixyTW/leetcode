class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        result: TLE
        naive solution: calculate all container water
        runtime: O(n^2), space: O(1)
        """
        # maxArea = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         x = j-i
        #         y = min(height[i], height[j])
        #         maxArea = max(maxArea, x*y)
        # return maxArea
        """
        result: Accepted
        sliding window: 
        2 indexes starting from the left, right most side 
        2 indexes approach each other until two indexes meet
        runtime: O(n), space: O(1)
        """
        l, r = 0, len(height)-1
        maxArea = 0
        while l < r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea
            