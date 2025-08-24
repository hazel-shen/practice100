from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0, -1)] # Initialize the directions
        max_island_area = 0
        island_area = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    grid[x][y] = -1 # visited
                    queue.append((x, y))
                    island_area = 0

                    while queue:
                        noder, nodec = queue.popleft()
                        island_area += 1
                        for r, c in directions:
                            nr = noder + r
                            nc = nodec + c 
                            if rows > nr >= 0 and cols > nc >= 0 and grid[nr][nc] == 1:
                                grid[nr][nc] = -1
                                queue.append((nr, nc))

                    max_island_area = max(max_island_area, island_area)

        return max_island_area