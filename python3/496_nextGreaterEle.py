class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {num:-1 for num in nums1}
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            if num in dic:
                stack.append(num)
        ans = [dic[num] for num in nums1]
        return ans