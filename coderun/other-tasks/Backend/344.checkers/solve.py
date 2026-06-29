# WA на 5 закрытом тесте (id: 7)
def find_capture(n, m, white_positions, black_positions, current_turn):
    board = [[0] * m for _ in range(n)]
    for x, y in white_positions:
        board[x - 1][y - 1] = 1
    for x, y in black_positions:
        board[x - 1][y - 1] = 2

    if current_turn == 'white':
        directions = [(1, 1), (1, -1)]
        my_piece, oponent_piece = 1, 2
    else:
        directions = [(-1, 1), (-1, -1)]
        my_piece, oponent_piece = 2, 1

    for x in range(n):
        for y in range(m):
            if board[x][y] == my_piece:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    ex, ey = x + 2 * dx, y + 2 * dy
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == oponent_piece:
                        if 0 <= ex < n and 0 <= ey < m and board[ex][ey] == 0:
                            return "Yes"
    return 'No'

def main():
    n, m = map(int, input().split())
    k_w = int(input())
    white_positions, black_positions = [], []
    for _ in range(k_w):
        pos = tuple(map(int, input().split()))
        white_positions.append(pos)
    k_b = int(input())
    for _ in range(k_b):
        pos = tuple(map(int, input().split()))
        black_positions.append(pos)
    current_turn = str(input())
    print(find_capture(n, m, white_positions, black_positions, current_turn))

if __name__ == '__main__':
    main()
