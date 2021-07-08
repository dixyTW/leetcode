class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        result: accepted
        pattern: We know the the permuation follows a certain order (ascending)
        If there is a way (formula) to predict at kth permutation what the permutation would look like,
        we don't have to get all permutations to get the kth permutation
        Note that for n numbers, each number is responsible for (n-1)! permutations
        Example: n = 3
        1: 123, 132
        2: 213, 231
        3: 312, 321
        Using this pattern, we can slowly get each level (first number) of the permutation.
        runtime: O(n^2), space: O(n)
        """
        nums = [x for x in range(1,n+1)]
        def helper(lst, n, k):
            if n == 1:
                return lst[0]
            fac = math.factorial(n-1)
            index, rem = divmod(k, fac)
            num = lst[index]
            lst.remove(num)
            return num*(10**(n-1)) + helper(lst, n-1, rem)
        ans = helper(nums, n, k-1)
        return str(ans)