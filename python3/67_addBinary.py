class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        result: accepted
        same approach as addOne
        runtime: O(max(a,b)^2) due to strin concatenation, space: O(1)
        """
        carry = 0
        i1, i2 = len(a)-1, len(b)-1
        ans = ""
        while i1 >= 0 or i2 >= 0:
            Sum = carry
            if i1 >= 0:
                Sum += int(a[i1])
                i1 -= 1
                
            if i2 >= 0:
                Sum += int(b[i2])
                i2 -= 1
            carry, num = divmod(Sum, 2)
            ans = str(num) + ans
        if carry:
            ans = str(carry) + ans 
        return ans