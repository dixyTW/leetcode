class Solution:
    def trap(self, height: List[int]) -> int:
        """
        result: accepted
        stack solution:
        traverse the heights, we have three cases
        1. if height[i-1] > height[i] (descending), we store height[i-1] info for potential water trapping
        2. if height[i-1] < height[i] (ascending), we start popping the stack and collecting water using height[i] as a reference height. When the height in the stack is the same or greater than the height of height[i].
        runtime: O(n), space: O(n)
        """
        stack = [] #stores height, index
        ans = 0
        for i in range(1, len(height)):
            if height[i-1] > height[i]:
                stack.append((height[i-1], i-1))
            if height[i-1] < height[i]:
                prev_h = height[i-1]
                while stack:
                    if stack[-1][0] <= height[i]:
                        h, index = stack.pop()
                        high = min(h, height[i])-prev_h
                        width = i - index - 1
                        ans += high*width
                        prev_h = min(h, height[i])
                    else:
                        #keeping the elevation for future use
                        h, index = stack[-1]
                        high = min(h, height[i])-prev_h
                        width = i - index - 1
                        ans += high*width
                        prev_h = min(h, height[i])
                        break        
        return ans