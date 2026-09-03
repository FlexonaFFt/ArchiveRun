import sys

n, t = map(int, input().split())
moves = map(int, input().split())

rows = [0] * n
cols = [0] * n
main_diag = 0
side_diag = 0

for round_number, cell in enumerate(moves, start=1):
    row = (cell - 1) // n
    col = (cell - 1) % n

    rows[row] += 1
    cols[col] += 1

    if row == col:
        main_diag += 1
    if row + col == n - 1:
        side_diag += 1

    if (rows[row] == n or cols[col] == n
            or main_diag == n or side_diag == n):
        print(round_number)
        break
else:
    print(-1)
