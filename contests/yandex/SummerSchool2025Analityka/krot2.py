class Solution:
    def yaGolodny(self, n: int, e: int, s: int) -> float:
        if e == s:
            return 0.0  # Если уже в кладовке

        dp = [0.0] * n  # DP-массив для хранения ожиданий шагов

        for i in range(n):
            if i == s:
                continue  # Кладовка - цель

            expectation = 0.0
            for step in range(1, n):  # Проход по всем возможным ходам
                next_pos = (i + step) % n  # Движение по кругу
                probability = (n - step) / n  # Вероятность
                expectation += probability * (1 + dp[next_pos])  # Считаем ожидание

            dp[i] = expectation / sum((n - step) / n for step in range(1, n))  # Усреднение

        return dp[e]  # Возвращаем значение для начальной позиции


def test():
    solution = Solution()
    print(solution.yaGolodny(3, 2, 1))  # Ожидание
    print(solution.yaGolodny(4, 1, 3))  # Ожидание


def main():
    solution = Solution()
    n, e, s = map(int, input().split())
    print(solution.yaGolodny(n, e, s))


if __name__ == '__main__':
    test()
