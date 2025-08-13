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
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        
        stack = []
        stack.append((sr,sc))

        image[sr][sc] = newColor
        while(stack):
            oldr, oldc =  stack.pop()
            for r, c in directions:
                nr = oldr + r
                nc = oldc + c
                if rows > nr >= 0 and cols > nc >= 0 and image[nr][nc] == oldColor:
                    image[nr][nc] = newColor
                    stack.append((nr, nc))
        
        return image
        