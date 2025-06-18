class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(0, len(matrix) - 1):
            for j in range(0, len(matrix[i]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

# Runtime 0 ms, 100 %
# Memory 17.56 mb, 99.57 %
def test():
    solve = Solution()
    print(solve.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(solve.isToeplitzMatrix([[1,2],[2,2]]))

if __name__ == '__main__': test()
