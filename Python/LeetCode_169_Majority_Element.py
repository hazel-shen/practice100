class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer–Moore
        candidate = nums[0]
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 0

            if (nums[i] == candidate) != 0: # 不一樣
                count -= 1
            else:  # 一樣
                count += 1


            
        return candidate
        
nums = [4,4,1,2,4,3]
s = Solution()
print(s.majorityElement(nums))