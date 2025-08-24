from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat or not mat[0]:
            return mat

        rows, cols = len(mat), len(mat[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)] # Initialize the directions
        queue = deque()

        for x in range(rows):
            for y in range(cols):
                if mat[x][y] == 0:
                    queue.append((x,y)) # Put all zeros into queue
                else:
                    mat[x][y] = 9999 # set infinite distance for verifying distance

        while queue:
            nx, ny = queue.popleft() 
            for dx, dy in directions:
                newx = nx + dx
                newy = ny + dy
                if 0 <= newx < rows and 0 <= newy < cols and mat[newx][newy] > mat[nx][ny] + 1:
                    mat[newx][newy] = mat[nx][ny] + 1
                    queue.append((newx, newy))
        
        return mat


