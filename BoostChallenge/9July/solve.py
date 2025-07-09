def solve(ballad: str, n: int) -> int:
    s = [c for c in ballad if c != ' ']
    n = len(s)
    # Для каждой буквы будем хранить количество вхождений до текущей позиции
    from collections import defaultdict

    # Считаем сколько раз каждая буква встречается справа от текущей позиции
    total = [0] * 26
    for c in s:
        total[ord(c) - ord('a')] += 1

    ans = 0
    left = [0] * 26  # сколько раз буква встречалась слева

    for mid in range(n):
        c_mid = ord(s[mid]) - ord('a')
        total[c_mid] -= 1  # текущая буква теперь не справа

        # Для всех букв a: считаем пары (a, s[mid], a)
        for a in range(26):
            ans += left[a] * total[a]

        left[c_mid] += 1  # текущая буква теперь слева

    return ans

