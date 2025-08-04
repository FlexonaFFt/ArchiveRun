from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right, fruit in enumerate(fruits):
            count[fruit] += 1

            # Если типов фруктов больше двух, сдвигаем левую границу окна
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            # Обновляем максимум
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

