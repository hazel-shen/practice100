class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4 # if land, then set 4 as perimeter
                    if rows > r+1 >= 0 and grid[r+1][c] == 1: # subsctract 2 if bottom neighbor is land 
                            perimeter -= 2
                    if cols > c+1 >= 0 and grid[r][c+1] == 1: # subsctract 2 if right neighbor is land 
                            perimeter -= 2
        
        return perimeter
