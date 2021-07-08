class Solution:
    def longestAwesome(self, s: str) -> int:
        """
        result: accepted
        bit manipulation: keep track of all seen mask bits in a dictionary (could use a size 1024 array as well).
        Suppose i < j, and at point i we get mask x, and at point j we get mask x as well. That means all chars within i to j have even counts, which is a palindrome if we can switch the characters around
        For the odd cases of palindrome, we flip the bits off within the mask, if we can flip 1 bit and get a seen mask, that means the string is a palindrome as well
        runtime: O(n), space: O(1)
        """
        dic = collections.defaultdict(int)
        dic[0] = -1
        ans = 0
        mask = 0
        for i, c in enumerate(s):
            num = int(c)
            mask = mask ^ (1 << num)
            
            if mask in dic:
                ans = max(ans, i-dic[mask])
            for n in range(10):
                #deal with palindrome with odd length
                if mask ^ (1 << n) in dic:
                    ans = max(ans, i - dic[mask^(1<<n)])
            if mask in dic:
                dic[mask] = min(dic[mask], i)
            else: 
                dic[mask] = i
        return ans