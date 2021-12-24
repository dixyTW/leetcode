class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def helper(nums):
            #returns the number of operations to make the array increasing
            lst = []
            for num in nums:
                if not lst or lst[-1] <= num:
                    lst.append(num)
                else:
                    index = bisect_right(lst, num)
                    lst[index] = num
            return len(lst)
        ans = 0
        visited = set()
        for i in range(k):
            lst = []
            for j in range(i, len(arr), k):
                lst.append(arr[j])
            ans += len(lst)-helper(lst)
        
        return ans