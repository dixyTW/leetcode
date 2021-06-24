class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        result: accepted
        brute force: sort all strings and match them
        runtime: sorting each word m*nlog(n), space: O(n) 
        """
        # dic = collections.defaultdict(list)
        # for str in strs:
        #     sorted_str = "".join(sorted(str))
        #     dic[sorted_str].append(str)
        # return list(dic.values())
        
        """
        result: accepted
        improve on brute force: instead of sorting strings using default sort function, we construct a sort function.
        runtime: n*m, space: O(n) 
        """
        def helper(s):
            #helper function that returns a sorted word
            lst = [0 for _ in range(26)]
            for c in s:
                lst[ord(c)-ord('a')] += 1
            ret = ""
            for i, num in enumerate(lst):
                for _ in range(num):
                    ret += chr(i+ord('a'))
            return ret
        
        dic = collections.defaultdict(list)
        for str in strs:
            sorted_str = helper(str)
            dic[sorted_str].append(str)
        return list(dic.values())