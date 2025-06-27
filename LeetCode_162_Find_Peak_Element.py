# 主要是要一邊透過左右比較的方式縮小尋找的範圍
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right :
            index = ( left + right ) // 2
            if nums[index] < nums[index+1]:
                left = index + 1 # 右邊可能有 peak
            elif nums[index] > nums[index+1]:
                right = index # 包含index 的左邊可能有 peak

        return right