class Solution:
    from typing import List
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0]) if len(board) > 0 else 0
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for dr, dc in moves:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                        live_neighbors += 1

                if board[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][col] = -1
                else:
                    if live_neighbors == 3:
                        board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == -1:
                    board[row][col] = 0

        return board


# Runtime 0 ms, 100 %
# Memory 17.70 mb, 75.83 %
def main():
    solution = Solution()
    print(solution.gameOfLife(board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

if __name__ == '__main__':
    main()
