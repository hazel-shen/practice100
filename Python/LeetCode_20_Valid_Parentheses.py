class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        result = False

        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        if s == "":
            return True

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != mapping[c]:
                    return False

        return len(stack) == 0

sol = Solution()
result = sol.isValid("}{()")
print(result)
