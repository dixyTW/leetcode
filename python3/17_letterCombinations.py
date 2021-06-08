class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        result: Accepted
        naive solution: try every solution
        runtime: O(3^n), space: O(1)
        """
        if not digits:
            #empty case solution []
            return []
        ans = []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def helper(string, cur):
            if not string:
                ans.append(cur)
            else:
                for c in dic[string[0]]:
                    helper(string[1:], cur+c)
        
        helper(digits, "")
        return ans