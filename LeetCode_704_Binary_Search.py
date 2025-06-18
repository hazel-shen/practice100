class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            index = (left + right) // 2

            if nums[index] == target:
                return index

            if nums[index] < target:
                left = index + 1
            elif nums[index] > target:
                right = index - 1
                
        # 當 left > right 就代表所有 item 都比較過了，然而沒有人相等
        return -1
