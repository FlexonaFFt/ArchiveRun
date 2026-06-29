class Solution:
    from typing import List
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        # Транспонирование матрицы
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Отображение матрицы по вертикали
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        return matrix

# Runtime 0 ms, 100 %
# Memory 17.78 mb, 55.18 %
def main():
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution = Solution()
    print(solution.rotate(matrix=matrix1))
    print(solution.rotate(matrix=matrix2))

if __name__ == '__main__':
    main()
