class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = float('-inf') # negative infinite number
        temp = 0.0
        for i, n in enumerate(nums):
            if i > k - 1:
                temp = temp + nums[i] - nums[i-k]
            else:
                temp = temp + nums[i] # keep accumulating
            if i >= k - 1 and temp > max_sum:
                max_sum = temp

        return max_sum / k
        