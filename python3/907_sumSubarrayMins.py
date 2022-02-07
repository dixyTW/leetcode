class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        left, right = [0 for _ in range(N)], [0 for _ in range(N)]
        l_stack, r_stack = [], []
        ans = 0
        mod = 10**9 + 7
        
        cnt = 0
        for i in range(N):
            cnt = 1
            while l_stack and arr[i] <= l_stack[-1][0]:
                cnt += l_stack.pop()[1]
            l_stack.append([arr[i], cnt])
            left[i] = cnt
        
        for i in range(N-1, -1, -1):
            cnt = 1
            while r_stack and arr[i] < r_stack[-1][0]:
                cnt += r_stack.pop()[1]
            r_stack.append([arr[i], cnt])
            right[i] = cnt
        
        for i in range(N):
            ans += left[i]*right[i]*arr[i]
        return ans % mod 
            