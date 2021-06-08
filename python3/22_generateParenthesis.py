class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        result: accepted
        dfs solution: 
        we build a helper function that puts valid strings into the answer list
        The helper function keeps track of the number of open parentheses (op) that are availible
        and the number of closing parentheses (cl) that can be inserted into the current string             (cur). When both op and cl are zero, that means there are no longer any chars left for us to         insert into the string, we have finished building a well-formed parentheses string
        runtime: O(2^n), space: O(1)
        """
        self.ans = []
        def helper(cur, op, cl):
            if not op and not cl:
                self.ans.append(cur)
                return
            if op:
                helper(cur+"(", op-1, cl+1)
            if cl:
                helper(cur+")", op, cl-1)
        helper("", n, 0)
        return self.ans
        