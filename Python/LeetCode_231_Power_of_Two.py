class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        if n & (n - 1) != 0:
            return False
        else:
            return True
        