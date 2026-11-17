from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and board[i][j] == "O":
                    board[i][j] = "#"
                    q.append([i,j])
        
        while q:
            top = q.popleft()
            I, J = top[0], top[1]
            if board[max(0,I-1)][J] == "O":
                board[I-1][J] = "#"
                q.append([I-1, J])
            if board[I][max(0, J-1)] == "O":
                board[I][J-1] = "#"
                q.append([I, J-1])
            if board[min(I+1, n-1)][J] == "O":
                board[I+1][J] = "#"
                q.append([I+1, J])
            if board[I][min(m-1, J+1)] == "O":
                board[I][J+1] = "#"
                q.append([I, J+1])
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"