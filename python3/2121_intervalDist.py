class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        """
        prefix_sum + binary search
        """
        ans = []
        prefix_sum = defaultdict(list)
        dic = defaultdict(list)
        
        for i, num in enumerate(arr):
            dic[num].append(i)
            if num not in prefix_sum:
                prefix_sum[num].append(0)
            prefix_sum[num].append(prefix_sum[num][-1]+i)
        for i, num in enumerate(arr):
            index = bisect_left(dic[num], i)
            leng = len(dic[num])
            Sum = prefix_sum[num][-1] - prefix_sum[num][index] - (i * (leng-index)) + (index*i) - prefix_sum[num][index]
            ans.append(Sum)
        return ans
            