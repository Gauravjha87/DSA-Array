class Solution(object):
    def threeSum(self, nums):

        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):

            # skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                # skip duplicate left
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                # skip duplicate right
                if right < n - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result


        