class Solution(object):
    def searchRange(self, nums, target):

        #first occurence 
        n = len(nums)
        low = 0
        high = n-1
        first = -1

        while(low<=high):
            mid = low + (high-low) // 2
            if (nums[mid] == target):
                first = mid
                high = mid - 1
            elif (nums[mid] < target):
                low = mid+1
            else: 
                high = mid-1

        #last occurence

        low = 0
        high = n - 1
        last = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1
        
        return [first, last]

        
        
        