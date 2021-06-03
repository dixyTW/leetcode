class Solution:
    def intToRoman(self, num: int) -> str:
        """
        result: accepted
        solution: 
        create a value -> roman mapping map
        subtract the number by the largest possible roman number
        runtime: O(len(lst)^2), space: O(len(lst))
        """
        lst = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        dic = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

        ans = ""
        while num:
            for n in lst:
                if num >= n:
                    num -= n
                    ans += dic[n]
                    break
        return ans