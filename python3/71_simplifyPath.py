class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        result: AC
        stack solution: parse out all "/" and "."
        Always pop 2 tokens because we always insert 2 elements ("/" and directory name)
        check for empty stack for edge case
        runtime: O(n), space: O(n)
        """
        stack = []
        tokens = [t for t in path.split("/") if t != "." and t != ""]
        for token in tokens:
            if token == "..":
                if stack:
                    stack.pop()
                    stack.pop()
            else:
                stack.append("/")
                stack.append(token)
        if not stack:
            return "/"
        else:
            return "".join(stack)