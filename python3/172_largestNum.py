class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        mergesort
        """
        def mergesort(n):
            if len(n) <= 1:
                return n
            l = mergesort(n[:len(n)//2])
            r = mergesort(n[len(n)//2:])
            i, j = 0, 0
            lst = []
            while i < len(l) and j < len(r):
                if l[i] + r[j] > r[j] + l[i]:
                    lst.append(l[i])
                    i += 1
                else:
                    lst.append(r[j])
                    j += 1
            lst += l[i:] if i < len(l) else r[j:]
            return lst
        nums = [str(n) for n in nums]
        ans = "".join(mergesort(nums))
        return ans if int(ans) != 0 else "0"
            
    
            