class Solution:
    def max_active_sections(self, s: str) -> int:
        if not s:
            return 0

        t = '1' + s + '1'
        max_active = s.count('1')  # Изначальное количество '1'

        # Находим все блоки '1', окруженные '0' в t
        n = len(t)
        one_blocks = []
        i = 1
        while i < n - 1:
            if t[i] == '1' and t[i-1] == '0' and t[i+1] == '0':
                start = i
                while i < n - 1 and t[i] == '1':
                    i += 1
                one_blocks.append((start, i - 1))
            else:
                i += 1

        # Если нет подходящих блоков '1', возвращаем исходное количество
        if not one_blocks:
            return max_active

        # Для каждого блока '1' выполняем trade
        for (start, end) in one_blocks:
            # Шаг 1: Заменяем блок '1' на '0'
            new_t = t[:start] + '0' * (end - start + 1) + t[end+1:]

            # Шаг 2: Ищем самый длинный блок '0', окруженный '1'
            zero_blocks = []
            i = 1
            while i < len(new_t) - 1:
                if new_t[i] == '0' and new_t[i-1] == '1' and new_t[i+1] == '1':
                    zero_start = i
                    while i < len(new_t) - 1 and new_t[i] == '0':
                        i += 1
                    zero_blocks.append((zero_start, i - 1))
                else:
                    i += 1

            # Если нет подходящих блоков '0', пропускаем
            if not zero_blocks:
                continue

            # Выбираем самый длинный блок '0'
            best_zero_start, best_zero_end = max(zero_blocks, key=lambda x: x[1] - x[0] + 1)
            zero_length = best_zero_end - best_zero_start + 1

            # Шаг 3: Заменяем этот блок '0' на '1'
            # Но нам не нужно реально менять строку, достаточно посчитать:
            # Новое количество '1' = исходное - (длина блока '1', который заменили) + (длина блока '0', который заменили)
            current_active = max_active - (end - start + 1) + zero_length
            max_active = max(max_active, current_active)

        return max_active


def test():
    solution = Solution()
    print(solution.max_active_sections(s='01'))
    print(solution.max_active_sections(s='0100'))
    print(solution.max_active_sections(s='1000100'))

test()
