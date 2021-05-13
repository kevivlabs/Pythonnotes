class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    #leetcode 53
        if not nums:
            return 0
        
        best=nums[0] 
        total_sum =nums[0]
        for i in nums[1:]: # we dont take into account the first in the list
            total_sum = max(i,total_sum+i)
            best= max(best,total_sum)
            
        return  best


#kadane's algorithm but doesnt work when its fully negative integers
