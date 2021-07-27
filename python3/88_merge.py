class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        result: AC
        explanation:
        we move all numbers in nums1 to the right so we have space at the begining of nums1 to insert into
        then we use 2 pointers to determine the smaller element between nums1 and nums2
        runtime: O(n), space: O(1)
        """
        for i in range(m-1, -1, -1):
            nums1[i+n] = nums1[i]
        i = 0
        l, r = n, 0
        while i < len(nums1) and l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                nums1[i] = nums1[l]
                l += 1
            else:
                nums1[i] = nums2[r]
                r += 1
            i += 1
        while l < len(nums1):
            nums1[i] = nums1[l]
            l += 1
            i += 1
        
        while r < len(nums2):
            nums1[i] = nums2[r]
            r += 1
            i += 1
        