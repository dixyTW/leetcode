class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        seat_lst = [i for i, c in enumerate(corridor) if c == "S"]
        ans = 1
        M = len(seat_lst)
        if M % 2 or M < 2:
            return 0
        for i in range(M//2 - 1):
            ans = (ans * (seat_lst[i*2+2] - seat_lst[i*2+1]))%mod
        return ans
            