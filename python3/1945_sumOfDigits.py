class Solution:
    def getLucky(self, s: str, k: int) -> int:
        Sum = ""
        for c in s:
            Sum += str(ord(c) - ord('a') + 1)
        Sum = int(Sum)
        while k > 0:
            newSum = 0
            for n in str(Sum):
                newSum += int(n)
            k -= 1
            Sum = newSum
        return Sum