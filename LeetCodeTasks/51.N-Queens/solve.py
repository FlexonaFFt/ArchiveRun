class Solution:
    from typing import List
    def solveQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                    return False
            return True

        def backtrack(row):
            if row == n:
                solutions.append(["".join(["Q" if i == col else "." for i in range(n)]) for col in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

        solutions = []
        board = [-1] * n
        backtrack(0)
        return solutions

# Runtime 33 ms, 27.14 %
# Memory 18.14 mb, 81.94 %
def main():
    solution = Solution()
    print(solution.solveQueens(n=4))

if __name__ == '__main__':
    main()
