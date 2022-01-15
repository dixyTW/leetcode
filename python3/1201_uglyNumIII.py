class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def helper(num):
            total = num//a + num//b + num//c
            ab = num//lcm(a,b)
            ac = num//lcm(a,c)
            bc = num//lcm(b,c)
            abc = num//lcm(a, lcm(b,c))
            return total - ab - ac - bc + abc
        
        
        def lcm(n1,n2):
            return (n1*n2)//math.gcd(n1,n2)
        
        # binary search
        l, r = 0, min(a,b,c)*n
        res = None
        while l <= r:
            mid = (l+r)//2
            count = helper(mid)
            if count >= n:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            
        
        
    
        
        # TLE
#         ans = min(a,b,c)
#         mult = [1,1,1]
#         cands = [a,b,c]
#         k = len(cands)
#         for i in range(n):                
#             ans = min([cands[j]*mult[j] for j in range(k)])
#             mult = [mult[j] + (mult[j]*cands[j] == ans) for j in range(k)]
#         return ans

     
        
            