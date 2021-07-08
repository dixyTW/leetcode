class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0 for _ in range(n+1)]
        if n <= 2:
            return n
        mem[1] = 1
        mem[2] = 2
        for i in range(3, n+1):
            mem[i] = mem[i-1] + mem[i-2]
        return mem[-1]