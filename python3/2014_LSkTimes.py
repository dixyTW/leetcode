class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        consider all possible candidate (a candidate is a alphabet that can appear in s k times)
        check all permutations formed by these candidates
        """
        counter = Counter(s)
        cands = sorted([key for key in counter if counter[key] >= k])
        q = deque([""])
        ans = ""
        def helper(ss):
            # returns True if ss is a valid subsequence that repeats k times in s
            i = 0
            cnt = 0
            for c in s:
                if c == ss[i]:
                    i += 1
                if i == len(ss):
                    cnt += 1
                    if cnt == k:
                        return True
                    i = 0
            return False 
        while q:
            cur = q.popleft()
            for c in cands:
                new_cur = cur+c
                if helper(new_cur):
                    ans = new_cur
                    q.append(new_cur)
        return ans
        