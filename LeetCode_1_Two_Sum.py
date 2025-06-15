class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = 0
        hash_map = {}
        for i, n in enumerate(nums):
            hash_map[target - nums[i]] = i # target - nums[i] 要是某個 nums 的值, i 則是位置
                                           # 所以 key 得是值, value 是位置
                
        for i, n in enumerate(nums):
            if n in hash_map and i != hash_map[n]: 
                return [ i, hash_map[n]]


sol = Solution()
nums = [2, 7, 11, 15]
target = 9
res = sol.twoSum(nums, target)
print(res)