class Solution:
    def maxWater(self, n, data):
        l = [0]*(n+1)
        r = [0]*(n+1)
        a = [0]*(n+1)
        for i in range(1, n+1):
            l[i], r[i], a[i] = data[i-1]

        best = 0
        for start in range(1, n+1):
            total = a[start]
            flow = 10**18
            for j in range(start-1, 0, -1):
                flow = min(flow, l[j+1])
                if flow == 0:
                    break
                total += min(a[j], flow)

            flow = 10**18
            for j in range(start+1, n+1):
                flow = min(flow, r[j-1])
                if flow == 0:
                    break
                total += min(a[j], flow)

            best = max(best, total)
        return best

'''
if __name__ == "__main__":
    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    sol = Solution()
    print(sol.maxWater(n, data))'''

if __name__ == "__main__":
    # Примеры из условия
    n1 = 3
    data1 = [(0, 10, 5), (0, 10, 2), (0, 0, 1)]
    print(Solution().maxWater(n1, data1)) # ожидаем 8


    n2 = 3
    data2 = [(0, 2, 3), (4, 0, 4), (1, 0, 5)]
    print(Solution().maxWater(n2, data2)) # ожидаем 7


    # Дополнительные тесты
    # 1 резервуар
    n3 = 1
    data3 = [(0, 0, 10)]
    print(Solution().maxWater(n3, data3)) # ожидаем 10


    # 2 резервуара, большой канал
    n4 = 2
    data4 = [(0, 100, 5), (100, 0, 7)]
    print(Solution().maxWater(n4, data4)) # ожидаем 12 (оба можно заполнить)


    # 2 резервуара, маленький канал
    n5 = 2
    data5 = [(0, 1, 5), (1, 0, 10)]
    print(Solution().maxWater(n5, data5)) # ожидаем 6 (ограничение канала)


    # 4 резервуара, разные каналы
    n6 = 4
    data6 = [(0, 5, 3), (2, 2, 6), (4, 1, 8), (7, 0, 10)]
    print(Solution().maxWater(n6, data6)) # проверка сложного случая
