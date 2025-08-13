class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        newColor = color

        if oldColor == newColor:
            return image

        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if not (rows > r >= 0 and cols > c >= 0): return
            if image[r][c] != oldColor: return

            image[r][c] = newColor 

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        
        return image
        