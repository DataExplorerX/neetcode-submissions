from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        viz = [[False for _ in range(m)] for _ in range(n)]
        q = deque()
        islands = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and viz[i][j] == False:
                    viz[i][j] = True
                    islands += 1
                    q.append([i, j])
                    while q:
                        top = q.popleft()
                        I, J = top[0], top[1]
                        if grid[max(0, I-1)][J] == "1" and viz[max(0, I-1)][J] == False:
                            viz[I-1][J] = True
                            q.append([I-1, J])
                        if grid[min(n-1, I+1)][J] == "1" and viz[min(n-1, I+1)][J] == False:
                            viz[I+1][J] = True
                            q.append([I+1, J])
                        if grid[I][max(0, J-1)] == "1" and viz[I][max(0, J-1)] == False:
                            viz[I][J-1] = True
                            q.append([I, J-1])
                        if grid[I][min(m-1, J+1)] == "1" and viz[I][min(m-1, J+1)] == False:
                            viz[I][J+1] = True
                            q.append([I, J+1])
        return islands



        