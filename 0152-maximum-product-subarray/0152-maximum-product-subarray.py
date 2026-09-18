class Solution(object):
    def maxProduct(self, nums):

        minending = nums[0]
        maxending = nums[0]
        ans = nums[0]
        n = len(nums)

        for i in range(1, n):
            c1 = nums[i]
            c2 = minending * nums[i]
            c3 = maxending * nums[i]

            maxending = max(c1, c2, c3)
            minending = min(c1, c2, c3)

            ans = max(ans, maxending)

        return ans       
        