class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        possible maximum gap cases:
        1. min max in the same bucket
        2. max of previous bucket and min of the proceeding non-empty bucket
        
        """
        ans = 0
        Max, Min = max(nums), min(nums)
        if Min == Max:
            return ans
        b_size = math.ceil((Max - Min)/(len(nums)-1))
        buckets = collections.defaultdict(list)
        for num in nums:
            buckets[(num-Min)//b_size].append(num)
        cur = float('inf') #to not count the initial bucket_min - cur case (min(nums)-0)
        for i in range(len(nums)):
            if i in buckets:
                if len(buckets[i]) >= 1:
                    bucket_max, bucket_min = max(buckets[i]), min(buckets[i])
                    ans = max(ans, bucket_max - bucket_min, bucket_min - cur)
                    cur = bucket_max
        return ans
                    