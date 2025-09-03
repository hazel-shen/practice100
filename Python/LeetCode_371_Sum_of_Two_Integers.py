class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF       # 限制為 32 位元 (用來模擬整數溢出)
        MAX  = 0x7FFFFFFF       # 32 位元有號整數的最大值 (0111...111)

        # 將 a, b 限制在 32 位元內
        # 這樣就能模擬 C/Java 中固定長度整數的行為
        a &= MASK
        b &= MASK

        # 迴圈直到沒有進位 (carry)，第一次的迴圈其實 SUM 就算好了，後續都是為了接下來的 ripple carries
        while b != 0:
            # ^ 表示「不進位加法」(XOR)
            # XOR 只負責相加但不考慮進位
            s = (a ^ b) & MASK

            # & 表示「計算進位」
            # (a & b) 找到需要進位的位置，再左移一位就是進位值
            c = ((a & b) << 1) & MASK

            # 更新 a, b
            # a 先存 XOR 結果，b 存進位值
            a, b = s, c
        
        # 迴圈結束時，b == 0，a 就是最終的和
        # 接下來要處理「有號整數」和「無號整數」的差異

        if a <= MAX:
            # 如果結果 <= MAX (2147483647)，代表是正數，可以直接回傳
            return a
        else:
            # 如果結果大於 MAX，代表是負數
            # Python 沒有固定 32 位元整數，需要把它轉換回「補數表示」
            # ~(a ^ MASK) 等效於將 32 位元補數轉回 Python 的負數
            return ~(a ^ MASK)
