class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)
        for i in range(l):
            K = []
            L = []
            for j in range(l):
                if board[i][j].isdigit(): K.append(board[i][j])
                if board[j][i].isdigit(): L.append(board[j][i])
        
            if len(K) != len(set(K)): return False
            if len(L) != len(set(L)): return False

        for r in range(0, l, 3):
            for c in range(0, l, 3):
                N = []
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j].isdigit(): N.append(board[r+i][c+j])
                if len(N) != len(set(N)): return False

        return True

