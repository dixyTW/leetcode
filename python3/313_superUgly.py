class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        h = [(1,max(primes))]
        num, fact = 0, 0
        for _ in range(n):
            num, fact = heappop(h)
            for x in primes:
                if x <= fact:
                    heappush(h, (x*num, x))
        return num