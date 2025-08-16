class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for x in range(0, rows):
            for y in range(0, cols):
                if grid[x][y] == 1:
                     for r, c in directions:
                        nr, nc = x + r,y + c
                        if rows <= nr or nr < 0 or cols <= nc or nc < 0:
                            perimeter += 1
                        elif grid[nr][nc] == 0:
                            perimeter += 1

        return perimeter
