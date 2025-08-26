class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b