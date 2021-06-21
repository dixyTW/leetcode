class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        result: TLE
        naive solution: try every path
        runtime: O(n^2), space: O(n)
        """
#         mem = [float("inf") for _ in range(len(nums))]
#         mem[0] = 0
#         for i, num in enumerate(nums):
#             for j in range(1,i+num+1):
#                 if j >= len(nums):
#                     break
#                 mem[j] = min(mem[j], mem[i]+1) #update every path's shortest possible jumps
#         return mem[-1]
    
        """
        result: accepted
        Greedy solution: 
        We need to know minimum step of i-1 to know minimum steps for i 
        Use a dictionary to keep track of the maximum coverage of number of steps (first step covers num[0])
        Graph representation:
        case: [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
        what we want: [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2] (minimum steps required to reach index i)                                              
        runtime: O(n), space: O(n)
        """
        # if len(nums) <= 1:
        #     return 0
        # steps = 1
        # dic = collections.defaultdict(int) 
        # dic[1] = nums[0]
        # for i in range(1, len(nums)):
        #     if dic[steps] < i:
        #         steps += 1
        #     dic[steps+1] = max(dic[steps+1], i+nums[i])
        # return steps 
        """
        constant space solution
        """
        if len(nums) <= 1:
            return 0
        steps, furthest = 1, nums[0]
        next_furthest = 0 #furthest distance steps+1
        for i in range(1, len(nums)):
            if furthest < i:
                steps += 1
                furthest = next_furthest
            next_furthest = max(next_furthest, i+nums[i])
        return steps