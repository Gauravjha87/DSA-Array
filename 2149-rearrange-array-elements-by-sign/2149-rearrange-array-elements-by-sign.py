class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n
        posindex, negindex = 0, 1 

        for i in range(0, n):
            if nums[i]>=0:
                result[posindex] = nums[i]
                posindex+=2
            else:
                result[negindex] = nums[i]
                negindex+=2

        return result
        