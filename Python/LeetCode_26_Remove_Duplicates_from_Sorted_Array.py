class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number_so_far = nums[0]
        new_stack = [nums[0]]
        if not nums:
            return 0

        for n in nums:
            if new_stack[-1] != n:
                new_stack.append(n)

        nums[:] = new_stack
        return len(nums)

sol = Solution()
nums = [1, 2, 3, 4, 4, 4, 4]  
length = sol.removeDuplicates(nums)
print("result length of  nums =", length)
print("nums[:length] =", nums[:length])