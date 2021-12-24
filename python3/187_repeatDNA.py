class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        result: AC
        method: get all substring from s and use a dicitonary to keep track of the substrings we've seen, return all substrings that have a count > 1
        runtime: O(N), space: O(N)
        """
        dic = collections.defaultdict(int)
        lst = collections.deque([c for c in s[:10]])
        dic[''.join(lst)] += 1
        ans = []
        for i in range(10, len(s)):
            lst.popleft()
            lst.append(s[i])
            dic[''.join(lst)] += 1
        for key, val in dic.items():
            if val > 1:
                ans.append(key)
        return ans 
            
        