class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            res <<= 1
            res |= (n & 1)
            n >>= 1
        return res