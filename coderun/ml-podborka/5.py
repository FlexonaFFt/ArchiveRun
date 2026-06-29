import numpy as np 

class Solution:

    def main(self, n, m, k, A, B):
        rows, rhs = [], []
        for i in range(n - k + 1):
            for j in range(m - k +1):
                row = []

                for t in range(k):
                    for l in range(k):
                        row.append(A[i + t][j + l])
                rows.append(row)
                rhs.append(B[i][j])

        x = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)[0]
        C = np.round(x).astype(int).reshape(k, k)
        for row in C: print(' '.join(map(str, row)))


    def func(self) -> None:
        n, m, k = map(int, input().split())
        A, B = [], [] 

        for _ in range(n):
            A.append(list(map(int, input().split())))

        for _ in range(n - k + 1):
            B.append(list(map(int, input().split())))
        self.main(n, m, k, A, B)


if __name__ == '__main__':
    Solution().func()