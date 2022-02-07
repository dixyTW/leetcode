class Solution:
    def minimumSum(self, num: int) -> int:
        def helper(l, seen, permList):
            SET = set({"0","1","2","3"})
            if not l or l in seen:
                return
            l_lst, r_lst = [], []
            r = "".join(c for c in SET - set(l))
            genPerm(l,"",l_lst) 
            genPerm(r,"",r_lst) 
            seen.add(l)
            
            # create pairs of possible permutations
            for pat1 in l_lst:
                for pat2 in r_lst:
                    permList.append([pat1,pat2])
            
            for i in range(len(l)):
                helper(l[:i]+l[i+1:], seen, permList)
        
        def genPerm(s, cur, lst):
            # generate list of permutation for a given num string
            if not s:
                lst.append(cur)
                return
            for i in range(len(s)):
                genPerm(s[:i]+s[i+1:], cur+s[i], lst)
            
            
        permList = [] 
        ans = float('inf')
        helper("0123", set(), permList)
        num = str(num)
        
        for pat1, pat2 in permList:
            if pat1 and pat2:
                num1 = int("".join(num[int(i)] for i in pat1))
                num2 = int("".join(num[int(i)] for i in pat2))
                ans = min(ans, num1+num2)
        
        return ans
                
        
    