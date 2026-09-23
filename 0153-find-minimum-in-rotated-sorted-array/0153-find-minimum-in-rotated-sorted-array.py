class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                # Minimum is on the right
                low = mid + 1
            else:
                # Minimum is at mid or on the left
                high = mid

        return nums[low]
        