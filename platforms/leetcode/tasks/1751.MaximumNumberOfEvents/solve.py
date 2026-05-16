from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        # Step 1: Сортируем ивенты за все время
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Step 2: Извлекаем время начала для бинарного поиска
        start_times = [e[0] for e in events]

        # Step 3: Ебеним двумерный массив 
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Step 4: Смотрим каждый ивент
        for i in range(1, n + 1):
            start, end, value = events[i - 1]

            # Step 5: Прогоняем через бинарный поиск каждый подходящий промежуток времени
            prev = self.findLastNonOverlapping(events, i - 1, start)

            for j in range(1, k + 1):
                # Option 1: пропускаем ивент короче
                # Option 2: берем текущий ивент и добавляем его в prev best 
                dp[i][j] = max(dp[i - 1][j], dp[prev + 1][j - 1] + value)

        return dp[n][k]

    def findLastNonOverlapping(self, events, right, targetStart):
        left = 0
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if events[mid][1] < targetStart:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
