class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        result: accepted
        solution: speed up by making x^y -> (x^2)y/2
        runtime:O(log(n))
        """
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        if n % 2:
            return x*self.myPow(x, n-1)
        else:
            return self.myPow(x*x,n/2)