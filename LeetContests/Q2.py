class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = [[0 for _ in range(26)] for _ in range(rows)]
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0].upper()) - ord('A')
        row = int(cell[1:]) - 1

        if 0 <= row < self.rows and 0 <= col < 26:
            self.grid[row][col] = value
        else:
            raise ValueError("Cell reference out of bounds")

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        if not formula.startswith('='):
            raise ValueError("Invalid formula format")

        parts = formula[1:].split('+')
        if len(parts) != 2:
            raise ValueError("Formula must be of the form '=X+Y'")

        def evaluate_part(part):
            if part[0].isalpha():
                col = ord(part[0].upper()) - ord('A')
                row = int(part[1:]) - 1
                if 0 <= row < self.rows and 0 <= col < 26:
                    return self.grid[row][col]
                else:
                    return 0
            else:
                return int(part)

        return evaluate_part(parts[0]) + evaluate_part(parts[1])©leetcode
