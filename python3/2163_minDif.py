class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        left sum and right sum neeeds a minimum of n (N/3) elements 
        """
        N, n = len(nums), len(nums)//3
        l_heap, r_heap = [-n for n in nums[:n]], nums[N-n:]
        heapify(l_heap)
        heapify(r_heap)
        l_sum, r_sum = -sum(l_heap), sum(r_heap)
        l_lst, r_lst = [l_sum], [r_sum]
        
        #create l_lst, iterate from n to N-n
        for i in range(n, N-n):
            new_num = -nums[i]
            if new_num > l_heap[0]:
                l_sum += heappop(l_heap)
                heappush(l_heap, new_num)
                l_sum -= new_num
            l_lst.append(l_sum)
        
        #crate r_lst, iterate from N-n to n
        for i in range(N-n-1, n-1, -1):
            new_num = nums[i]
            if new_num > r_heap[0]:
                r_sum -= heappop(r_heap)
                heappush(r_heap, new_num)
                r_sum += new_num
            r_lst.append(r_sum)
        
        #get difference of l_lst, r_lst
        return min([a-b for a,b in zip(l_lst, r_lst[::-1])])
        
            
            
                                                  
        