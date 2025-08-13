class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return None

        last_index = len(numbers) - 1
        first_index = 0
        stack = []

        while first_index < last_index:
            _sum = numbers[first_index] + numbers[last_index]
            if target >  _sum:
                first_index += 1
            elif target <  _sum:
                last_index -= 1
            else:
                stack.append(first_index + 1)
                stack.append(last_index + 1)
                break
                
        return stack
numbers = [1, 2, 2, 3, 4]
target = 6
sol = Solution()
rs = sol.twoSum(numbers, target)
print(rs)