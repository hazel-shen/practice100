class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = {}
        start = 0
        max_length = 0
        for i, c in enumerate(s):
            if (sub.get(c, -1) >= start): 
                # 如果目前這個字元上次的位置（sub.get(c, -1)）大於等於 start，代表在 window 中遇到重複的字母了

                # 把 window 開頭移到上次出現的重複字母的下一個位置
                start = sub[c] + 1
            
            sub[c] = i # 更新一下目前字元的位置

            # 嘗試用目前 window 的長度 (i - start + 1) 更新最大長度，
            # 因為只要 window 是合法的（字元不重複），就有可能是最長的子字串
            max_length = max(max_length, i - start + 1) 
        
        return max_length
            

