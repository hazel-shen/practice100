class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        count_a = len(a) - 1
        count_b = len(b) - 1
        carry = 0
        result = []

        while count_a >= 0 or count_b >= 0 or carry != 0:
            digit_a = int(a[count_a]) if count_a >= 0 else 0
            digit_b = int(b[count_b]) if count_b >= 0 else 0
   
            summary = digit_a + digit_b + carry
            carry = summary // 2
            digit = summary % 2
            result.append(digit)
            count_a -= 1
            count_b -= 1
        
        result.reverse()
        return "".join(map(str, result))