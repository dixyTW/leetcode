class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []
        ans = [-1 for _ in range(N)]
        
        for i, num in enumerate(nums):
            
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            if ans[i] == -1:
                stack.append(i)
        
        for i, num in enumerate(nums):
            
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            if ans[i] == -1:
                stack.append(i)
        return ans