import math

class Solution:
    def transpose(self, matrix):
        return list(map(list, zip(*matrix)))

    def matmul(self, A, B):
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def gauss_solve(self, A, b):
        n = len(A)
        for i in range(n):
            max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            for j in range(i + 1, n):
                ratio = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= ratio * A[i][k]
                b[j] -= ratio * b[i]

        x = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = b[i]
            for j in range(i + 1, n):
                x[i] -= A[i][j] * x[j]
            x[i] /= A[i][i]
        return x

    def calculator(self, n: int, data: list):
        X_features, Y = [], []

        for x, fx in data:
            t1 = math.tan(x)
            s = math.sin(x)
            c = math.cos(x)
            t4 = math.sqrt(x)
            X_features.append([t1, s ** 2, s * c, c ** 2, t4])
            Y.append(fx)

        XT = self.transpose(X_features)
        XTX = self.matmul(XT, X_features)
        XTY = self.matmul(XT, [[y] for y in Y])
        XTY = [row[0] for row in XTY]

        coeffs = self.gauss_solve(XTX, XTY)

        a = coeffs[0]
        A = coeffs[1]
        B = coeffs[2]
        C = coeffs[3]
        d = coeffs[4]

        b = (1 if B >= 0 else -1) * math.sqrt(A)
        c = B / (2 * b)
        print(f"{a:.2f} {b:.2f} {c:.2f} {d:.2f}")


def main():
    solve = Solution()
    n = int(input())
    data = []
    for _ in range(n):
        x, fx = map(float, input().split())
        data.append((x, fx))
    solve.calculator(n, data)


if __name__ == '__main__':
    main()
