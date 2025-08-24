from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)] # Initialize the directions
        island_count = 0
        queue = deque()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    grid[x][y] = "-1" # visited
                    island_count += 1
                    queue.append((x,y))

                    while queue:
                        nx, ny = queue.popleft()
                        for r, c in directions:
                            nr = nx + r
                            nc = ny + c
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "-1"
                                queue.append((nr,nc))


        
        return island_count


        