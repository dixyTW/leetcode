class Solution:
    def romanToInt(self, s: str) -> int:
        """"
        result: accepted
        solution: 
        keep a dictionary for roman to int mapping
        we traverse the string from right to left so we can know when to subtract or add 
        since we are traversing from right to left, we know the roman values should always be increasing
        unless we encounter special cases such as 4 (IV) or 9 (IX)
        in these cases, we know the "I" before "V" means to subtract 1 because now the symbols are in descending order
        compared to "VI" (6) or "XI" (11), these two are in ascending order in terms of roman values, so we add them together
        runtime: O(len(s)), space: O(1)
        """
        ans = 0
        Max = 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)-1, -1, -1):
            sym = s[i]
            val = dic[sym] if dic[sym] >= Max else -dic[sym]
            Max = max(dic[sym], Max)
            ans += val
        return ans
            