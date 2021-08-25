class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        result: AC
        greedy one pass: cur represents the current candy thats being added at index i
        case 1 ratings[i-1] < ratings[i]: add 1 to cur
        case 2 ratings[i-1] == ratings[i]: we can reset cur to 1
        case 3 ratings[i-1] > ratings[i]: lots of edge cases, check comments below
        runtime: O(n), space: O(1)
        """
        ans = 1
        i = 1
        cur = 1
        while i < len(ratings):
            if ratings[i] > ratings[i-1]:
                cur += 1 
                ans += cur
                i += 1
            elif ratings[i] == ratings[i-1]:
                cur = 1
                ans += cur
                i += 1
            else:
                start = i
                peak = cur #the peak, if 
                while i < len(ratings) and ratings[i] < ratings[i-1]:
                    """
                    idea as follows: a couple of cases to consider
                    1. [1,2,100,99,98...] peak value at 100 would normally be 3, but depending on the number of descending numbers that follows, that peak value (3) would have to change
                    2. regardless of this special case, if we encounter a descending sequence, we will have to add a total of (1+2..N) where N is the length of the desceding sequence
                    """
                    cur = (i-start+1) 
                    if cur >= peak:
                        # special case: 
                        cur = (i-start+2)
                    ans += cur
                    i += 1
                cur = 1 #reset cur to 1 since we are at the lowest point (a valley) and anything that comes after is guarunteed to be greater then ratings[i]
                        
        return ans