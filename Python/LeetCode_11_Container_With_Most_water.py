class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # area = (last_x - first_x) * min(height[first_x], height[last_x])
        first_x = 0
        last_x = len(height) - 1
        top_area = (last_x - first_x) * min(height[first_x], height[last_x])
        while first_x < last_x: # 找出最高的順便找出面積最大的
            
            if height[first_x] < height[last_x]:
                first_x += 1
            else:
                last_x -= 1

            new_area = (last_x - first_x) * min(height[first_x], height[last_x])
            if new_area > top_area:
                top_area = new_area

        return top_area
                
sol = Solution()
height = [1, 100, 1, 100, 1, 100]
res = sol.maxArea(height)
print(res)