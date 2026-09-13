class Solution(object):
    def pivotIndex(self, nums):
        
        left = 0
        total = sum(nums)
        n = len(nums)

        for i in range(0, n):
            right = total - nums[i] - left
            if(left == right):
                return i
            
            left += nums[i]
            
        return -1