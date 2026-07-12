class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # Check rows
        for i in range(n):
            seen = set()

            for j in range(n):
                if board[i][j] == '.':
                    continue

                if board[i][j] in seen:
                    return False

                seen.add(board[i][j])

        # Check columns
        for i in range(n):
            seen = set()

            for j in range(n):
                if board[j][i] == '.':
                    continue

                if board[j][i] in seen:
                    return False

                seen.add(board[j][i])

        # Check 3x3 boxes
        for row in range(0, n, 3):
            for col in range(0, n, 3):
                seen = set()

                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] == '.':
                            continue

                        if board[r][c] in seen:
                            return False

                        seen.add(board[r][c])

        return True