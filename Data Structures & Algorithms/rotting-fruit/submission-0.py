from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        final_time = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j,0])
        
        while q:
            top = q.popleft()
            I, J, time = top[0], top[1], top[2]
            final_time = time
            if grid[max(0, I-1)][J] == 1:
                grid[I-1][J] = 2
                q.append([I-1, J, time + 1])
            if grid[I][min(m-1, J+1)] == 1:
                grid[I][J+1] = 2
                q.append([I, J+1, time + 1])
            if grid[min(n-1, I+1)][J] == 1:
                grid[I+1][J] = 2
                q.append([I+1, J, time + 1])
            if grid[I][max(0, J-1)] == 1:
                grid[I][J-1] = 2
                q.append([I, J-1, time + 1])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return final_time
        


        