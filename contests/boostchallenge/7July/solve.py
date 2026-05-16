def solve(n: int, a: list[int], m: int, b: list[int]) -> int:
    # Двоичные последовательности, ищем LCS неубывающей подпоследовательности
    # Для 0 и 1 отдельно
    # Считаем количество 0 и 1 в обеих последовательностях
    a0 = [i for i, x in enumerate(a) if x == 0]
    b0 = [i for i, x in enumerate(b) if x == 0]
    a1 = [i for i, x in enumerate(a) if x == 1]
    b1 = [i for i, x in enumerate(b) if x == 1]
    # LCS из 0
    l0 = min(len(a0), len(b0))
    # LCS из 1
    l1 = min(len(a1), len(b1))
    # Теперь ищем максимальную длину неубывающей подпоследовательности
    # которая может быть вида: k0 нулей, потом k1 единиц
    # Переберём сколько нулей взять (от 0 до l0)
    res = 0
    # Префиксные массивы для ускорения
    # Для каждого k0: сколько единиц после k0 нулей
    # В a
    a0pos = []
    for i, x in enumerate(a):
        if x == 0:
            a0pos.append(i)
    a1cnt = [0] * (len(a0pos) + 2)
    for k0 in range(len(a0pos), -1, -1):
        if k0 == len(a0pos):
            start = len(a)
        else:
            start = a0pos[k0]
        a1cnt[k0] = a[k0 and a0pos[k0-1]+1 or 0 : start].count(1) + (a1cnt[k0+1] if k0+1 <= len(a0pos) else 0)
    # В b
    b0pos = []
    for i, x in enumerate(b):
        if x == 0:
            b0pos.append(i)
    b1cnt = [0] * (len(b0pos) + 2)
    for k0 in range(len(b0pos), -1, -1):
        if k0 == len(b0pos):
            start = len(b)
        else:
            start = b0pos[k0]
        b1cnt[k0] = b[k0 and b0pos[k0-1]+1 or 0 : start].count(1) + (b1cnt[k0+1] if k0+1 <= len(b0pos) else 0)
    for k0 in range(0, l0+1):
        # k0 нулей, потом сколько максимум единиц после этих нулей
        # В a: после k0 нулей, сколько единиц
        # В b: после k0 нулей, сколько единиц
        a1after = a1cnt[k0]
        b1after = b1cnt[k0]
        k1 = min(a1after, b1after)
        res = max(res, k0 + k1)
    return res

