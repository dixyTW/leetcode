class Solution:
    def numOfWays(self, n: int) -> int:
        """
        result: accepted
        DP + pattern: 3 blocks can be split into 2 categories, 1 with 2 colors (rbr, gbg ... etc) and 3 colors(rgb, gbr ....)
        Notice that there are a fixed number of color pattern that folows after the previous categories
        Assume the previous 3 blocks uses the 3 color pattern, the next layer of blocks can be split into 2 category: 2 color and 3 color
        Within the 2 color category, the list of patterns that uses 2 colors and also does not repeat colors is 2, and 3 for 3 colors
        This pattern works for if the previous layer is 2 color as well
        Using this information, we can deduce the total number of patterns 
        runtime: O(n), space: O(1)
        """
        p121, p123 = 6, 6
        for i in range(1, n):
            p121, p123 = p123*2 + p121*3, p123*2 + p121*2
            
        return (p121+p123)%(10**9+7)