class Solution(object):
    # Do it again
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        new = color
        if old == new:
            return image

        rows, cols = len(image), len(image[0])

        def expand_lr(y, x):
            """從 (y, x) 向左右擴展，回傳 (L, R)，前提：image[y][x] == old"""
            # 向左
            L = x
            while L - 1 >= 0 and image[y][L - 1] == old:
                L -= 1
            # 向右
            R = x
            while R + 1 < cols and image[y][R + 1] == old:
                R += 1
            return L, R

        def push_runs_in_row(y, L, R, stack):
            """在第 y 列的 [L, R] 區間內尋找 old 的連續子區段，把每段 (y, a, b) 推入 stack"""
            if not (0 <= y < rows):
                return
            x = L
            while x <= R:
                # 跳過非 old 的點
                while x <= R and image[y][x] != old:
                    x += 1
                if x > R:
                    break
                a = x
                # 往右延伸，直到不是 old
                while x <= R and image[y][x] == old:
                    x += 1
                b = x - 1
                # 把這段 [a, b] 當成新的種子段
                stack.append((y, a, b))

        # 主流程
        stack = []
        L0, R0 = expand_lr(sr, sc) 
        stack.append((sr, L0, R0))

        while stack:
            y, L, R = stack.pop()

            # 掃「上一列」和「下一列」的 run，並推入 stack（稍後處理）
            L2, R2 = expand_lr(y, L)

            for x in range(L2, R2 + 1):
                image[y][x] = new

            # 注意：此時先不要上色上一列/下一列；等它被 pop 出來時再上色
            push_runs_in_row(y - 1, L2, R2, stack)   # 尋找 y-1 列中的 old 區段
            push_runs_in_row(y + 1, L2, R2, stack)   # 尋找 y+1 列中的 old 區段


        return image
