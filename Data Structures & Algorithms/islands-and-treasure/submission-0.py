from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append([i,j])
        
        while q:
            top = q.popleft()
            I, J = top[0], top[1]
            if grid[max(0, I-1)][J] == INF:
                grid[I-1][J] = grid[I][J] + 1
                q.append([I-1, J])
            if grid[I][max(0, J-1)] == INF:
                grid[I][J-1] = grid[I][J] + 1
                q.append([I, J-1])
            if grid[min(I+1, n-1)][J] == INF:
                grid[I+1][J] = grid[I][J] + 1
                q.append([I+1, J])
            if grid[I][min(J+1, m-1)] == INF:
                grid[I][J+1] = grid[I][J] + 1
                q.append([I, J+1])