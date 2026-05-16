class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [[] for row in range(numRows)]
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)


def main():
    solution = Solution()
    print(solution.convert('PAYPALISHIRING', 4))

if __name__ == '__main__':
    main()
