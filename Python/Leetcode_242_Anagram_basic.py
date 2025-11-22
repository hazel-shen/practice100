# Time complexity: O(N)
# Space complexity: O(1)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        counts = [0] * 26

        # Get ASCII Code of 'a', for calculating offsets
        base_ord = ord('a')
        n = len(s)

        # for i in s:
        #     counts[ord(i) - base_ord] += 1

        # for i in t:
        #     counts[ord(i) - base_ord] -= 1

        for i in range(n):
            counts[ord(s[i]) - base_ord] += 1
            counts[ord(t[i]) - base_ord] -= 1

        for i in counts:
            if i != 0:
                return False
        
        return True



            
        