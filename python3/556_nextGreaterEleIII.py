class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        1. Find the first decreasing element n[i] starting from the right
        2. Get the next largest element from the compared to the decreasing element n[i], swap              
           the two elements n[i], n[j] = n[j], n[i]
        3. Reverse the right half of the array n[i+1:] = n[i+1:][::-1]
        """
        n = list(str(n))
        N = len(n)
        res = -1
        for i in range(N-2, -1, -1):
            if int(n[i]) < int(n[i+1]):
                index, dif = i, float('inf')
                for j in range(i+1, N):
                    if int(n[i]) < int(n[j]) and int(n[j]) - int(n[i]) <= dif:
                        # case: 12222333 make sure we get the right most 3 instead of the first 3
                        index, dif = j, int(n[j]) - int(n[i])
                n[i], n[index] = n[index], n[i]
                n[i+1:] = n[i+1:][::-1]
                
                res = int("".join(n))
                break
        if res >= 2**31:
            return -1
        return res 
        