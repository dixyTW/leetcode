class Solution:
    def reverseBits(self, n: int) -> int:
        """
        built in solution
        """
        # return int("{0:b}".format(n).zfill(32)[::-1],2)
        
        """
        loop through all bits in n one by one
        compare 32 times, but shift only 31 
        """
        ans = 0
        for i in range(31):
            ans = (ans | (n&0x1)) << 1 
            n >>= 1
        return ans | (n&0x1)