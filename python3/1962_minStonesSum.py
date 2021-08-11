class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        runtime: O(klogn), space: O(n)
        """
        Sum = sum(piles)
        h = []
        for num in piles:
            h.append(-num)
        heapq.heapify(h)
        while k > 0:
            num = -heapq.heappop(h)
            rem = num - math.floor(num/2)
            Sum -= math.floor(num/2)
            heapq.heappush(h,-rem)
            k -= 1
        return Sum
            
        