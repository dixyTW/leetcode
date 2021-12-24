class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        result: TLE
        brute force: use AND operation on every integer within left and right
        runtime: O(N), space: O(1)
        """
        # ans = 2**31 - 1
        # for num in range(left, right+1):
        #     ans &= num
        # return ans
        
        """
        result: AC 
        
        """
        if left == 0 or right == left:
            return left
        elif len(bin(left)) != len(bin(right)):
            return 0
        else:
            pref = 0x1 << math.floor(math.log2(left))
            return pref + self.rangeBitwiseAnd(left-pref, right-pref)

        