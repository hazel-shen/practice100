class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]

        for i in range(1, n+1):
            remainder = i % 2
            result.append(result[i >> 1] + remainder)
        
        return result

# s = Solution()
# r = s.countBits(10)
# print(r)