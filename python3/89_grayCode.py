class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        brute force
        runtime: 
        """
        # self.ans = []
        # def dfs(cur, seen, lst):
        #     if len(lst) == 2**n:
        #         self.ans = lst
        #         return True
        #     for i in range(n):
        #         newBit = cur ^ (0b1 << i)
        #         if newBit not in seen:
        #             seen.add(newBit)
        #             if dfs(newBit, seen, lst+[newBit]):
        #                 break
        #             seen.remove(newBit)
        #     return False
        # seen = {0}
        # dfs(0, seen, [0])
        # return self.ans
    
        """
        recursive solution
        runtime: O(2^n)
        """
        lst = [0]
        for i in range(n): 
            num = 2**i
            newlst = [x+num for x in lst]
            lst = [0] + newlst + lst[1:]
        return lst