class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []

        for i in range(0, numRows):
            row = [1]
            if i > 0:
                prev_row = res[-1]
                for j in range(1, i):
                    row.append(prev_row[j - 1] + prev_row[j])


                row.append(1)
            res.append(row)
        return res 


def test():
    solve = Solution()
    print(solve.generate(5))
    print(solve.generate(1))

if __name__ == '__main__':
    test()
