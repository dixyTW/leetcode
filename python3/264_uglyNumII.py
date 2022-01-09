class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # h = [(1,5)]
        # val, fact = 0, 0
        # for _ in range(1, n+1):
        #     # fact helps prevent duplicates
        #     # 5 can be paired with 5,3,2
        #     # 3 can be paiired with 3,2
        #     # 2 can only be paired with 2
        #     # 55, 53, 52, 33, 32, 22 
        #     val, fact = heappop(h)
        #     for x in (2,3,5):
        #         if fact >= x:
        #             heappush(h, (val*x, x))
        # return val
        nums = [1]
        cands = [2,3,5]
        indexes = [0,0,0]
        k = len(cands)
        for i in range(n-1):
            new_nums = [cands[j]*nums[indexes[j]] for j in range(k)]
            new_num = min(new_nums)
            nums.append(new_num)
            for j in range(k):
                indexes[j] += (nums[indexes[j]]*cands[j] == new_num)
        return nums[-1]
                