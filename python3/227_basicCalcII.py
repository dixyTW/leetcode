class Solution:
    def calculate(self, s: str) -> int:
        #parse input
        s = s.replace(" ", "")
        tokens = []
        prev = 0
        for i in range(len(s)):
            if s[i] in "+-/*":
                tokens.append(s[prev:i])
                tokens.append(s[i])
                prev = i + 1
        tokens.append(s[prev:])
        
        q = deque([])
        N = len(tokens)
        i = 0
        ans = 0
        while i < N:
            # if we see numbers or +,- add it to the q
            # if we see /,* process the tokens until there are no more /,*
            t = tokens[i]
            if t == "+" or t == "-" or t.isnumeric():
                q.append(t)
                i += 1
            else:
                # / or *
                left = int(q.pop())
                while i < N and (tokens[i] != "+" and tokens[i] != "-"):
                    if tokens[i] == "/":
                        left = left // int(tokens[i+1])
                        print(s[i+1])
                    if tokens[i] == "*":
                        left *= int(tokens[i+1])
                    i += 2
                q.append(str(left))
        while q:
            t = q.popleft()
            if t.isnumeric():
                ans += int(t)
            else:
                num = q.popleft()
                if t == "-":
                    ans -= int(num)
                else:
                    # plus
                    ans += int(num)
        return ans
                    
            
                    