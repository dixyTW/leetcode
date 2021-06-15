class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        result: accepted
        some observations: there will always be a pivot, and nums[0] > nums[-1] for all cases
        modified binary search: slice the lst into 2, one that is in normal order (ascending), 
        and the other contains the pivot. Always check the normal lst first, if the target is in
        the normal lst, we discard the pivot lst. Otherwise we chose the pivot lst, and repeat the rocess
        runtime: O(logn), space: O(1)
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[l] <= nums[mid]:
                    if nums[l] <= target < nums[mid]:
                        r = mid-1
                    else:
                        l = mid+1
                if nums[mid] <= nums[r]:
                    if nums[mid] < target <= nums[r]:
                        l = mid+1
                    else:
                        r = mid-1
        return -1