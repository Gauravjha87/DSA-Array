class Solution(object):
    def subarraySum(self, nums, k):

        sum = 0
        freq = {0: 1}
        res = 0
        n = len(nums)

        for i in range(0, n):
            sum = sum+nums[i]
            ques = sum - k

            res = res + freq.get(ques, 0)
            freq[sum] = freq.get(sum, 0) + 1

        return res


        
        