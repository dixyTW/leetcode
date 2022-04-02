class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def helper(num, length, pos):
            if length == 0:
                # base case
                return 0
            elif length == 1:
                # base case
                return num*(10**pos)
            else:
                # (length-1//2) because we want to get the correct base number
                # length = 1,2 we want base number 1
                # length = 3,4 we want base number 10 and so on
                base = 10**(max(0,(length-1)//2))
                n, newNum = divmod(num,base)
            if intLength == length:
                # n+1 because in order to form a valid palindrome, our outer numbers needs to
                # be from 1-9, 10 is not possible since we ruled them out in the beginning                       # (max_base)
                return (n+1)*(10**(length-1)) + (n+1) + helper(newNum, length-2, pos+1)
            else:
                return n*(10**(length-1+pos)) + n*(10**pos) + helper(newNum, length-2, pos+1)
                
        ans = []
        # if query number exceeds max_base, this means it is not possible to form a palidnrome
        max_base = int(10**((max(0,intLength-1)//2)) * 9) 
        if intLength == 1:
            # handles special case, not sure how to handle every case in the helper function                 # without making it ugly
            return [x if x < 10 else -1 for x in queries]
        for n in queries:
            if n > max_base:
                ans.append(-1)
            else:
                # queries number starts from 0 instead of 1 (n-1)
                res = helper(n-1, intLength, 0)
                ans.append(res)
        return ans