# This way will be faster than using max() function.
# Due to less function calls overhead.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]
        for i, n in enumerate(nums[1:]):
            if current_sum < 0:
                current_sum = n
            else:
                current_sum += n

            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum
        